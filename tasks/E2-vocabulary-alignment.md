# E2 — Minimal vocabulary alignment decision record

Status: ready after V01 closeout publication; research not started. Owner: research assistant, semantic decisions reviewed by project owner.

## Objective

Produce a small source-linked crosswalk for the accepted draft pilot, not a replacement ontology or automatic upstream mapping. Distinguish role concepts, capabilities, implementation definitions/revisions, deployments, executions and provenance assertions.

## Read scope

AGENTS.md; docs/STATE.md; docs/plan-v0.2.md; docs/architecture-v0.1.md; docs/pilot-role-contracts.md; schema/role-contract.schema.json; examples/roles/*.json; existing AgentO research and validation reports. Read authoritative SKOS and PROV-O specifications and exact previously inspected AgentO terms as needed. Record document version/section, retrieval date and precise term URI. Do not run extractors or retrieve imports automatically.

## Proposed write scope

docs/research/vocabulary-alignment-v0.1.md; reports/design/vocabulary-alignment-v0.1.json; tasks/REPORT-TEMPLATE.md-based report under reports/design; docs/plan-v0.2.md; docs/STATE.md. No schema, canonical vocabulary or implementation registry mutation in this task. Publication needs exact-write approval.

## Deliverable

For each of role concept/label, responsibility versus capability, definition revision, deployment, execution, provenance assertion and review status: project meaning; candidate external URI or explicit absence; source evidence; fit/mismatch; reuse/project-specific/defer recommendation; rationale; review state. Include concrete examples from the three pilot roles. Separate vocabulary semantics from validation tooling: LinkML selection is not decided by term similarity.

## Acceptance and limits

Every external candidate has a source-linked definition and explicit fit assessment. Do not invent URIs, claim equivalence from names, or use exactMatch as a generic similarity link. Keep responsibility specification distinct from observed capability; distinguish a software artifact from its execution and deployment. Record capability-modelling gaps rather than force a match. No third-party ontology copying or relicensing; reference terms and preserve evidence. Explain how each proposed reuse affects later records, without implementing new fields.

Stop on unresolved semantic conflict, missing exact source evidence or unclear rights for copying. A useful completion can recommend defer. No graph server, dependency installation, model API, paid Runtime compute, live configuration changes, upstream prompt ingestion, automatic merge or deployment. After two failed attempts at the same step, report evidence and next action.
