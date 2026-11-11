# Restart checkpoint

Updated: 11 November 2026, 14:39 NZDT. This file describes the proposed foundations commit; confirm its publication in Git before marking it done.

## Read order

1. AGENTS.md
2. docs/STATE.md
3. docs/plan-v0.2.md
4. The assigned task packet
5. Supporting architecture/research evidence as needed

Git and checked task reports are durable state; chat memory is not authoritative. Verify current branch and working tree before changes.

## Repository and publication

Public: https://github.com/GeniusTechnoMystic/agent-role-ontology. Last confirmed remote commit before this proposed update: 69758242ee5c90c6983213ea67d07b6fee948d7c. Earlier: 8c3fd25 initial checkpoint; 1960411 AgentO review; f66e7c7 archive addendum and architecture/plan. The previous downloadable bundle was not itself committed. This update preserves its substantive repository files, not its packaging wrapper. GitHub is available in the current message; future workers must rediscover tools rather than assume persistent availability.

## Settled direction

Harness-neutral discovery/routing ontology with upstream implementation registry, not prompt hosting. Roles are tool-neutral responsibility contracts. Technologies/methods are facets; prompts are replaceable implementations. Distinguish roles, capabilities, definitions, conversions, deployments, executions, and evaluations. Disclose dependencies, paid/proprietary services, authority, environment assumptions, and data flows. Hard policy constraints precede ranking; unknown is explicit. Trends are discovery signals, not trust.

Prefer reuse over new software. Evaluate SKOS, PROV-O, LinkML, AgentO alignment, and Rulesync where appropriate; none is automatically adopted. No graph server, custom converter, package manager, or autonomous orchestrator yet.

Licensing decision: original ontology/vocabulary/metadata/documentation CC0-1.0 with voluntary attribution request; software MIT; third-party terms preserved. Standard texts and a complete scope map remain pending. Policy documentation is not a completed licence installation.

## Evidence completed

AgentO GitHub and archived ontology differ. DOI 18342624 resolves to record 18342625. Runtime downloaded the 7,573-byte ZIP independently; published MD5 matched. All three members matched uploaded SHA-256 hashes. RDFLib parsed 402 triples, 41 object properties, 13 datatype properties. Archive version 0.2 explicitly aligns with PROV-O/P-Plan but agentRole remains a string. No extractor execution, imports, reasoning, SHACL, or effectiveness test. Licence discrepancy unresolved. See reports/validation/2026-11-11-agento.json and docs/research/agento-runtime-validation.md.

## Runtime continuity

Ready image: agent-role-ontology-dev:v0.1, version 1; ID 516864d2-eeb7-45e2-922d-a6de8b844ec4. Sandbox 906105ba-d4c5-4f07-9503-b0641c880fc2 is stopped with disk retained. Do not wake without a bounded approved task. Python 3.12.16, RDFLib 7.1.4, PyYAML 6.0.2, jsonschema 4.23.0, pytest 8.3.5; pip check passed. Shared Dockerfile image tested, not full Dev Containers/Codespaces lifecycle. Direct pins are not a transitive lock. Retained storage may cost money. No model keys needed.

## Prepared work and next actions

This proposed commit contains F01 environment files, F03 worker/state docs, task packets, and S01 draft schema/examples. Three examples passed shape validation during preparation and six invalid cases were rejected; report is preparation evidence, not Runtime/CI validation. No schema is accepted as final; no upstream semantic equivalence or preferred implementation is asserted.

Next: verify this commit, finish F02 licences, review S01 here, and authorise I01 local input/export scope. V01 waits for schema acceptance. Do not repeat completed AgentO parsing absent changed inputs. No Copilot or local Kilo task has been started. Copilot entitlement/quota unknown; its Tasks connector exposed review/scanning only.

Unknowns: exact local collection contents/provenance, AgentO rights scope, role/capability granularity, LinkML suitability, other harness conversion compatibility. Keep unknowns rather than guess.
