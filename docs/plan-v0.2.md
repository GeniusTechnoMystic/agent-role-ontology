# Plan v0.2

Updated: 11 November 2026, 15:20 NZDT. Proposed publication against verified main HEAD 63b55b33efef38bf3a8cf0239e09a47d880e9044. This queue supersedes stale ordering in implementation-plan-v0.1.md. Architecture remains draft.

| Task | Status | Remaining gate |
|---|---|---|
| E1 AgentO archive/RDF validation | Complete at 6975824 | Rights uncertainty unresolved; no repeat without changed inputs |
| F01 Development environment | Published at 9f9fffc; image smoke-tested | Full Dev Containers/Codespaces lifecycle untested; pins not a transitive lock |
| F02 Standard licences/scope | Installation published at 63b55b3 | Third-party clearance not implied; byte-identical upstream CC0 download not independently verified |
| F03 Worker rules/checkpoint | Published; refreshed in this changeset | Successful publication and ongoing maintenance |
| D01 AI disclosure/copyright identity | Published at 6e6d80c | Model label owner-reported, not independently verified |
| I01 Mechanical local inventory | Awaiting local read/export approval | Private output scope; no local task launched |
| S01 Role-contract pilot | Limited direction owner-accepted at 15:15; hardening locally checked and included here | Successful publication; concepts remain draft |
| V01 Offline validation CI | 85 local checks passed; suite/workflow included here | Publish; obtain actual successful GitHub Actions result before marking complete |
| E2 Vocabulary alignment | Pending | Source-linked crosswalk and explicit reuse decision |
| I02 Structured inventory | Not task-ready | I01 plus explicit parser/schema |
| C01 Evidence extraction | Not task-ready | Fixed vocabulary and approved inputs; proposals only |
| R01 Resolution fixtures | Pending | Reviewed mappings and explained selection/failure |

## Sequence

Publish this changeset after exact approval. Observe the GitHub Actions run for the resulting commit; do not call a prepared workflow a passing run. I01 may proceed separately only after local scope approval. E2 can inform later schema work without silently adopting external vocabularies. Broader ontology acceptance remains pending.

## Boundaries

No Runtime wake, paid compute, local configuration changes, automatic merge/deploy, or upstream prompt publication was performed. Use maintained tools before custom software. Verify Copilot entitlement before assignment. Defer graph servers, custom converters/installers, embeddings, trend automation and multi-harness execution until required. Use task allowlists and stop after two failed attempts at a step.

Latest evidence: reports/design/role-contract-hardening-validation.json. Tests use pytest/jsonschema and reject test-time socket networking. Workflow setup still requires network for checkout, Python and dependency installation. Action tags are documented major-version tags, not immutable SHA pins. Update STATE.md with actual publication/run evidence when available.
