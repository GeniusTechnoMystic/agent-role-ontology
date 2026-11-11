# V01 — Offline role-contract validation CI

Blocked until owner accepts S01 schema/examples. Worker: eligible Copilot workflow or local Kilo; entitlement unknown. Inputs: approved schema/role-contract.schema.json, examples/roles/*.json, requirements-dev.txt, AGENTS.md. Designated branch only. Allowed writes: tests/test_role_contracts.py and .github/workflows/validate.yml. No schema edits without separate task.

Use pytest/jsonschema, not a custom validator or model API. Test schema validity, all examples, and negative cases: missing ID, invalid prefix, empty purpose, missing criteria, unexpected property, empty responsibilities. Do not weaken schema to pass tests.

CI: contents:read only, no secrets/write tokens/pull_request_target, bounded timeout, dependency install from approved requirements. No upstream agent downloads; tests run offline. Select supported Actions versions from current authoritative guidance; never invent commit SHAs.

Acceptance: python -m pytest -q passes, negatives tested, count/output captured. Validate workflow syntax with an existing tool if available; otherwise state unvalidated. No claims of reasoning, reference integrity, routing quality, or complete devcontainer lifecycle. Stop after two failed attempts per step. No deploy or auto-merge.
