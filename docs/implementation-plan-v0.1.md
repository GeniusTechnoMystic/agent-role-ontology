# Delivery and local-agent plan v0.1

Status: proposed tasks and gates; no execution claimed. Date: 11 November 2026.

## Working rules

Reuse existing solutions before custom code. Work outside live harness configuration. Never publish a local snapshot before sensitive-content and rights review. Local auto-routed agents execute small evidence tasks; they do not invent canonical concepts, approve mappings, merge changes, or activate deployments. Escalate uncertainty rather than guessing.

Every task report: task ID; exact input revisions/digests; actions; changed paths; commands and exit statuses; validation results; evidence; unresolved questions. Capture actual model identifier when observable; otherwise mark unknown. A session label is not proof of a fixed underlying model.

## M0 — Project foundations

Research assistant: refine design and policies. Owner: approve scope and significant trade-offs. Add unmodified CC0 and MIT texts, licence-scope map, attribution request, contribution policy, and agent work boundaries. Acceptance: clear original/third-party separation; no implication that upstream prompts are relicensed. No software implementation yet.

## M1 — Verify reuse and evidence

Local task E1: work in a new scratch directory containing only the supplied AgentO files; calculate hashes, parse Turtle with an existing RDF parser, list explicit classes/properties/alignments, and capture errors. Do not run extractor/run_prompt.py, fetch imports, or install tools without authorisation. Use a parser's output to check terms, not a handwritten regex parser. Report reasoning separately; parsing success is not ontology correctness.

Research task E2: compare AgentO artefacts and competing discovery/registry approaches against architecture requirements. Check licence scope and exact versioned terms. Acceptance: source-linked fit/gap matrix and an explicit reuse/extend/align decision; no conclusion based on filename or star count alone.

## M2 — Read-only local inventory

Owner approves input paths and export scope. Local task I1 inventories selected installed definitions and upstream checkouts: relative paths, symlink targets, source commits where available, full-file SHA-256, prompt-body digest with a documented normalisation method, frontmatter, resource references, permissions, model values, and read/parse failures. Report unknown conversion provenance as unknown. Exclude credentials, unrelated files, and raw prompt publishing.

Local task I2 reports exact-byte duplicate groups, body-equal/config-different groups, and duplicate runtime names. Do not delete, rename, overwrite, infer semantic equality, or resolve local references by guessing. Acceptance: every approved input accounted for; deterministic checks reproducible; zero live changes.

## M3 — Minimal schema and curated pilot

Research assistant authors role contracts, vocabulary IDs, evidence/mapping records, and a minimal schema trial using existing tooling. Curate a small representative set covering reviewer, test author, security assessor, and implementation alternatives. Include both accepted and deliberately invalid examples.

Local task S1 runs prescribed validators and records output; task S2 extracts quotations for explicit candidate files against fixed vocabulary IDs. No new concepts or accepted equivalence assertions. Acceptance: records validate; unknown references and missing required evidence fail; proposals and accepted mappings remain separate; no requirement that every source maps successfully.

## M4 — Explainable resolution without installation

Create competency fixtures: offline/read-only review; missing authorised test environment; paid-service prohibition; unknown data-transfer requirement; unsupported conversion; missing supporting resource; independent reviewer requirement. Resolve by deterministic filtering plus reviewed selection before adding an LLM router.

Acceptance: each fixture yields an explained eligible selection, an approval requirement, or explicit failure. No silently dropped task requirement; no paid or unknown mandatory service under a deny policy; no popularity-based override; covered responsibilities and handoffs are visible. Start with records and reports, not a new daemon.

## M5 — One staged conversion path

Inspect installed Rulesync help/source for the exact version and approved format pair. Pin source definitions and converter version; review resources and licence. Convert only in an isolated staging root using existing tooling. Do not execute imported prompt instructions. Validate frontmatter, model IDs, paths, permissions, resources, and source-specific assumptions. Preserve original and generated digests plus reported semantic losses.

Acceptance: no writes outside staging; failed or unsupported conversion is reported; no implicit model aliases or expanded authority accepted; output discovery tested with explicit target harness version only when permitted. Compilation/discovery is not task-effectiveness evidence.

## M6 — Controlled deployment and evaluation

Owner approves exact files, destination, and permission profile. Local worker backs up, installs only owned artifacts, verifies discovery, and demonstrates rollback without removing unrelated agents. Evaluate with task fixtures and record model/harness/tools/permissions and evidence. Acceptance: unverified capabilities stay unverified; live changes separately approved; rollback tested; project claims match reproduced evidence.

## Deferred

Graph database, MCP/API service, embedding search, trending-feed automation, multi-harness deployment, auto-upgrades, complex optimiser, and full-team execution. Introduce only after the pilot identifies a concrete unmet need.

## Next bounded handoff

First execute E1 only after approving the local task environment. Return file hashes, RDF parser result, explicit role and alignment declarations, and unresolved licence/version questions. Do not fix AgentO, run its OpenAI extractor, or generate our entire ontology. This first task establishes trustworthy evidence for the architectural decision.
