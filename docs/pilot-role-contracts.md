# S01 — Provisional role-contract pilot

Owner accepted the limited direction on 11 November 2026 at 15:15 NZDT: retain three draft roles, reject whitespace-only text, defer larger ontology fields, and proceed with V01. This changeset publishes that direction; concepts remain draft, not canonical.

## Review conclusion

Code reviewer assesses proposed changes and returns evidence-linked findings. Test author translates requirements into assertions and returns test artifacts plus execution status. Security assessor evaluates risks inside authorised scope and returns evidence, assumptions and mitigations. Overlap is not equivalence. Multiple roles need not mean multiple processes; independent assurance requires an explicit workflow constraint, not merely distinct role names.

These remain tool-neutral draft concepts, not runtime prompts, upstream mappings, or evidence of measured capability. Retain status=draft. Acceptance of the pilot interface does not establish ontology-wide acceptance or a LinkML decision.

## Minimal hardening

Require at least one non-whitespace character in label, purpose and every item in the shared string-array definition. Preserve the identifier convention and existing constraints. Inputs/outputs remain descriptive strings, not machine-compatible artifact references. Whitespace handling follows the configured regex validator; no Unicode-normalisation policy is introduced.

## Explicitly deferred

Capability identifiers, typed artifact references, structured preconditions, evidence-bearing implementation mappings, machine-enforced independent-assurance relationships, and a broader lifecycle model need separate reviewed design. Do not infer graph integrity or routing compatibility from shape validation.

## Validation status

The baseline committed serialization at 9f9fffc passed schema self-validation, three examples and 18 invalid mutations in conversation Python. See reports/design/role-contract-committed-revalidation.json. The old preparation-only report is historical.

The hardened proposal passed 85 pytest checks during preparation: one schema self-check, three valid examples, 18 original negative cases and 63 whitespace-negative cases. See reports/design/role-contract-hardening-validation.json. These are local preparation results, not evidence that the published commit passed CI. Schema JSON formatting in this publication is compacted relative to the prepared bundle; constraints are unchanged. GitHub Actions and Runtime execution are not implied by local success.
