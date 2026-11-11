# S01 — Original draft role-contract pilot

Three tool-neutral illustrative roles and a JSON Schema shape are prepared, not accepted as canonical vocabulary. They are not runtime prompts, upstream mappings, or a LinkML adoption decision. JSON Schema uses existing validation tooling for a lightweight contract trial.

Roles represent responsibilities, not claims of measured capability. Review, test creation, and security assessment overlap but produce different outputs. Implementations may combine responsibilities except where independent assurance is required. Vendor/tool fields intentionally absent from core; profiles supply those details. Input/output strings are provisional labels, not graph IDs. Capability references, provenance assertions, facets, accepted status, and graph integrity checks are separate design work.

Owner/research review: Are boundaries useful? Inputs sufficient? Outputs observable? Which criteria need structured predicates? Do not map upstream agents by title alone.

Preparation checks passed for the earlier equivalent expanded shape: schema self-validation, three examples, six negative records. This commit factors repeated array definitions through local $defs/$ref without changing intended constraints; the committed serialization requires its own V01 revalidation. No CI, routing, reasoning, or task-effectiveness test ran.
