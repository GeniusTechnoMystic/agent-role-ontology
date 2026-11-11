# Plan v0.2

Date: 11 November 2026. New operational queue superseding stale ordering in implementation-plan-v0.1.md; architecture-v0.1.md remains draft.

| Task | Owner | State before this commit | Completion gate |
|---|---|---|---|
| E1 AgentO archive/RDF validation | Research assistant + Runtime | Complete, committed at 6975824 | Captured evidence; do not repeat without changed inputs |
| F01 Development environment | Research assistant | Prepared for this commit | Built configuration stored, lifecycle limits disclosed |
| F02 Standard licences/scope | Research assistant or repository worker | Task ready; not executed | Verified standard texts, explicit scope, optional credit |
| F03 Worker rules/checkpoint | Research assistant | Prepared for this commit | AGENTS, STATE, task-report template published |
| I01 Mechanical local inventory | Local Kilo | Awaiting local read/export approval | Reproducible raw hashes/provenance, no source changes |
| S01 Role-contract pilot | Research assistant + owner | Draft prepared and shape-checked | Three contracts and schema reviewed |
| V01 Offline validation CI | Eligible Copilot workflow or local Kilo | Blocked on S01 | Valid examples pass, invalid records fail offline |
| E2 Vocabulary alignment | Research assistant | Pending | Source-linked term crosswalk and reuse decision |
| I02 Structured frontmatter/body inventory | Local Kilo | Not task-ready; needs I01 and schema | Explicit parser/errors/normalisation |
| C01 Evidence extraction | Local Kilo | Not task-ready; needs fixed vocabulary and inputs | Three-to-five-file batch, quotations, proposals only |
| R01 Resolution fixtures | Research assistant | Pending reviewed contracts/mappings | Explained selection, approval, or failure |

## Sequence and accountability

Publish foundations; finish licensing; run I01 locally while S01 is reviewed here. Add V01 only after approval. Research assistant retains semantic boundaries and ambiguous decisions; workers collect evidence and run tests. Runtime is an independent validator, not ongoing background work.

Use existing tools before custom code. Verify Copilot plan feature access before assigning work; do not assume its connector launches coding agents. No automatic merges or deployments. Defer graph database, embeddings, custom installers/converters, trend automation, and multi-harness execution until a pilot demonstrates need.

## Recovery

Update STATE.md after meaningful checkpoints: last confirmed commit, task states, approvals, retained resources, unknowns, exact next action. A task packet must stand alone without the conversation. Review current Git state before applying prepared changes.
