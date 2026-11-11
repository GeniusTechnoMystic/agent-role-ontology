# Plan v0.2

Updated: 11 November 2026, 15:33 NZDT. Verified main HEAD: 409d786472563478b869430afe9643d3b4277a75. This queue supersedes implementation-plan-v0.1.md ordering; architecture remains draft. This closeout changeset itself awaits successful publication.

| Task | Status | Remaining work or limitation |
|---|---|---|
| E1 AgentO archive/RDF validation | Complete at 6975824 | Rights discrepancy unresolved; no repeat absent changed inputs |
| F01 Development environment | Published at 9f9fffc; image smoke-tested | Full editor/devcontainer lifecycle untested; pins not transitive lock |
| F02 Standard licences/scope | Published at 63b55b3 | Third-party clearance and byte-identical upstream CC0 download not implied |
| F03 Worker rules/checkpoint | Published; closeout refresh included here | Keep current after meaningful work |
| D01 AI disclosure/copyright identity | Published at 6e6d80c | Model label owner-reported, not independently verified |
| S01 Role-contract pilot | Limited direction accepted; hardening published at 409d786 | Concepts remain draft; broader ontology fields deferred |
| V01 Offline validation CI | Complete for 409d786: run 42946080836, attempt 1, success; 85 tests passed | Results do not certify future commits or semantic effectiveness |
| E2 Vocabulary alignment | Next task; packet prepared here, research not started | Source-linked crosswalk and explicit reuse/defer decisions |
| I01 Mechanical local inventory | Awaiting local read/export scope approval | Private output scope; no local task launched |
| I02 Structured inventory | Not task-ready | I01 plus parser/schema decisions |
| C01 Evidence extraction | Not task-ready | Fixed vocabulary and approved inputs; proposals only |
| R01 Resolution fixtures | Pending | Reviewed mappings and explained selection/failure |

## Next sequence

Publish this evidence/status update, then perform tasks/E2-vocabulary-alignment.md. Do not reopen S01 acceptance or rerun passing V01 merely to fill time. I01 can proceed separately only after explicit local scope approval. Broader ontology acceptance remains separate from pilot-interface acceptance.

## Evidence and boundaries

CI evidence: reports/validation/2026-11-11-role-contract-ci.json. Earlier local preparation evidence remains historical and distinct. All job steps, dependency installation, pip check and pytest succeeded in the inspected run. No workflow change, rerun, dispatch, Runtime wake, Copilot task, or local inventory execution was needed for closeout.

Use maintained tools first. Defer graph servers, custom converters/installers, embeddings and autonomous deployment. Preserve task allowlists, third-party rights and unknowns. No automatic merge/deploy or unapproved paid compute. Action major tags are mutable; dependency pins are not transitive lock. Tests block Python socket access, not operating-system networking; workflow setup needs network.
