# Development environment

Prepared Dockerfile was built as Runtime image agent-role-ontology-dev version 1. Runtime smoke checks and Turtle parsing passed; see reports/validation/2026-11-11-agento.json. Full Dev Containers/Codespaces lifecycle untested.

Python 3.12; RDFLib, PyYAML, jsonschema, pytest; Git and CA certificates. Non-root sandbox user. No model SDK, credentials, automatic upstream execution, privileged mode, Docker socket, or public service.

Repository devcontainer uses root build context and .devcontainer/Dockerfile, with /opt/venv preinstalled. Direct pins are not a transitive lock.

Runtime image ID: 516864d2-eeb7-45e2-922d-a6de8b844ec4. Resolved base: docker.io/library/python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df. Built rootfs SHA-256: d2a98a446550d9144baef54f4cbf1337348fa32cc0525214f05b9ea4c1cbd754. Dockerfile retains its tag; capture resolved digests on rebuild.

Checks: python -m pip check; python -m pytest -q once V01 exists. RDF parsing is not semantic correctness. Do not execute imported extractors or fetch external ontology imports during inspection. Private/artifact scratch data remains outside tracked publication pending review. LinkML/pySHACL are deferred evaluations.
