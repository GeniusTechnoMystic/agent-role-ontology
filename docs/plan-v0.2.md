# Plan v0.2

Updated: 11 November 2026, 15:06 NZDT. This operational queue supersedes stale ordering in implementation-plan-v0.1.md; architecture-v0.1.md remains draft. Statuses below describe this changeset once successfully committed.

| Task | Owner | Status | Remaining gate |
|---|---|---|---|
| E1 AgentO archive/RDF validation | Research assistant + Runtime | Complete at 6975824 | Do not repeat without changed inputs; upstream rights remain unresolved |
| F01 Development environment | Research assistant | Configuration published at 9f9fffc; image smoke-tested | Full Dev Containers/Codespaces lifecycle not tested; direct pins not transitive lock |
| F02 Standard licences/scope | Research assistant | MIT published at 6e6d80c; CC0, root selector, and scope map included here | Owner approval and successful publication of this changeset |
| F03 Worker rules/checkpoint | Research assistant | Published at 9f9fffc; checkpoint refreshed here | Keep current after meaningful work |
| D01 AI disclosure/copyright identity | Research assistant + owner | Complete at 6e6d80c | Model label is owner-reported, not independently verified |
| I01 Mechanical local inventory | Local Kilo | Awaiting explicit local read/export scope approval | Approved private output and reproducible provenance; no local task launched |
| S01 Role-contract pilot | Research assistant + owner | Draft published; committed shape revalidated: 3 valid, 18 invalid cases | Semantic review/acceptance; not canonical yet |
| V01 Offline validation CI | Eligible Copilot workflow or local Kilo | Blocked on S01 acceptance | Actual tests/workflow implemented and execution recorded |
| E2 Vocabulary alignment | Research assistant | Pending | Source-linked crosswalk and reuse decision |
| I02 Structured frontmatter/body inventory | Local Kilo | Not task-ready | I01 plus explicit parser/schema |
| C01 Evidence extraction | Local Kilo | Not task-ready | Fixed vocabulary and authorised inputs; proposals only |
| R01 Resolution fixtures | Research assistant | Pending | Reviewed contracts/mappings and explained selection/failure |

## Next sequence

Publish this status/licensing changeset; review S01 boundaries and structured-field needs here. Obtain explicit schema acceptance before V01. I01 may proceed independently only after local read/export approval. E2 research can inform S01 without silently adopting external terms. No ontology-wide acceptance, new worker launch, deployment, or Runtime wake is authorised by these statuses.

## Evidence and execution

See reports/design/role-contract-committed-revalidation.json for the recorded conversation-Python checks; these are not CI or Runtime results. The earlier preparation report remains historical, not latest status. Shared Dockerfile image was tested, not complete editor integration. Verify Copilot feature access before assignment; its availability is not established by a connector name.

Reuse maintained tools first. Defer graph servers, custom converters/installers, embeddings, trend automation, and multi-harness execution until demonstrated need. Use exact task allowlists, no automatic merge/deploy, and stop after two failed attempts at a step. Update STATE.md with commits, approvals, evidence, retained resources, unknowns, and next action.
