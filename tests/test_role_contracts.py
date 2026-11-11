# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Danny Poulson (GeniusTechnoMystic)
import copy
import json
import socket
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema/role-contract.schema.json").read_text())
PATHS = sorted((ROOT / "examples/roles").glob("*.json"))
VALIDATOR = Draft202012Validator(SCHEMA)
TEXT_FIELDS = ["label", "purpose", "responsibilities", "exclusions", "inputs", "outputs", "acceptance_criteria"]

@pytest.fixture(autouse=True)
def forbid_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("Network access is forbidden during validation tests")
    monkeypatch.setattr(socket, "socket", denied)
    monkeypatch.setattr(socket, "create_connection", denied)

def load(path):
    return json.loads(path.read_text())

def test_schema():
    assert PATHS, "No role examples discovered"
    Draft202012Validator.check_schema(SCHEMA)

@pytest.mark.parametrize("path", PATHS, ids=lambda p: p.stem)
def test_examples(path):
    VALIDATOR.validate(load(path))

@pytest.mark.parametrize("case", ["missing_id", "invalid_prefix", "empty_purpose", "missing_criteria", "unexpected_property", "empty_responsibilities"])
@pytest.mark.parametrize("path", PATHS, ids=lambda p: p.stem)
def test_negative_records(path, case):
    value = copy.deepcopy(load(path))
    if case == "missing_id":
        value.pop("id")
    elif case == "invalid_prefix":
        value["id"] = "invalid.software.code-review"
    elif case == "empty_purpose":
        value["purpose"] = ""
    elif case == "missing_criteria":
        value.pop("acceptance_criteria")
    elif case == "unexpected_property":
        value["unexpected"] = True
    else:
        value["responsibilities"] = []
    assert list(VALIDATOR.iter_errors(value)), case

@pytest.mark.parametrize("whitespace", [" ", "\t", "\n"])
@pytest.mark.parametrize("field", TEXT_FIELDS)
@pytest.mark.parametrize("path", PATHS, ids=lambda p: p.stem)
def test_whitespace_rejected(path, field, whitespace):
    value = copy.deepcopy(load(path))
    value[field] = whitespace if field in ("label", "purpose") else [whitespace]
    assert list(VALIDATOR.iter_errors(value)), (field, repr(whitespace))
