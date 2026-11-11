# Discovery architecture v0.1

Status: draft design, not implemented or validated. Date: 11 November 2026.

## Scope

Provide a harness-neutral semantic discovery layer: task -> capabilities/roles -> team plan -> eligible upstream implementations -> reproducible staged deployments. Do not become a prompt mirror, custom package manager, general orchestration engine, or assurance of upstream quality. Runtime execution remains the harness's responsibility.

Canonical roles specify purpose, responsibilities, inputs, outputs, preconditions, boundaries, evidence, and acceptance criteria. Vendors, executables, services, paths, and stack choices belong to profiles and implementations. Technology-specific expertise remains discoverable without contaminating the role core. A role contract is an interface specification, not a system prompt.

## Components and data flow

1. Vocabulary: functions, roles, capabilities, domains, technologies, methods, artifacts; definitions and inclusion/exclusion criteria.
2. Registry: source pointers, revisions, resources, licence evidence, assumptions, compatibility observations, and implementation-to-role assertions.
3. Discovery: retrieve candidate roles using vocabulary labels, facets, and evidence. Embeddings may later propose candidates, never establish equivalence.
4. Composition: assemble a proposed minimal adequate responsibility set, handoffs, dependencies, and required independent assurance. Multiple roles need not mean multiple processes.
5. Resolution: enforce user policy and environment compatibility before ranking eligible implementations. Return no compatible candidate when appropriate.
6. Materialisation: fetch approved pinned artifacts into quarantine/cache, verify digests, inspect resources, invoke an existing supported converter, validate outputs, stage a deployment manifest. Never run arbitrary upstream installers.
7. Activation: separately approved harness-specific install with backup, ownership records, and rollback.
8. Evaluation: retain observed model/harness/tool/task context and outcomes separately from source claims.

## Identity and graph

Use separate IDs for role, capability, upstream definition revision, conversion result, deployment, run, and evaluation. Runtime frontmatter names are deployment identifiers, not canonical role IDs. Label changes must not change identity. Source repository is provenance, not the primary taxonomy.

Proposed relationships: role requires capability; role specialises role; definition candidate-implementation-of role; definition requires dependency; conversion derived-from definition revision; deployment instantiates conversion; workflow step fulfils responsibility and hands-off artifact; evaluation assesses deployment/run.

Mappings are evidence-bearing assertions with subject, predicate, object, source revision/location, rationale, review status, reviewer, and timestamp. Keep exact artifact equality, prompt-body equality, conceptual similarity, and substitutability distinct. Require review before accepting semantic equivalence; close matches do not imply transitive equivalence.

Candidate reuse: SKOS for vocabularies, PROV-O for provenance, Dublin Core/SPDX identifiers for rights metadata, LinkML for schema/validation/export, Rulesync for supported conversion pairs, and AgentO/A2A crosswalks where meanings fit. These are evaluation targets, not blanket dependency approvals. A2A service cards and downloadable definitions remain distinct resource types.

## Record contracts

Role: stable ID; labels; purpose; responsibilities/exclusions; required capability IDs; input/output artifact types; preconditions; acceptance criteria; domain/method facets.
Definition revision: repository URL; commit; relative entry path; included resources; source format; per-artifact licence evidence; content digest; capability claims; dependencies; inspection scope.
Dependency: kind; mandatory/optional/conditional status; condition; version/platform constraints; accounts/costs; privileges; network/data handling; evidence and unknowns.
Compatibility observation: source and target formats/versions; converter/version/options; semantic losses; validation steps; result; tested environment. Distinguish format conversion, discovery test, and task effectiveness.
Resolution request: task; required responsibilities; environment capabilities; allowed services/data flows/authority; budget; target harness; policy version.
Resolution result: candidates and exclusion reasons; selected pinned definitions; uncovered requirements; approval requirements; handoffs; unresolved assumptions.
Lock record: source commits and digests, resources, adapter/version/options, policy and schema revisions, target profile, generated digests. Do not include credentials or claim identical future model behaviour.

## Policy and trust

Unknown is not false. Requirements have declared, inferred, or observed evidence and explicit inspection coverage. An undeclared dependency is not a verified absence. Evaluate mandatory and conditional requirements against environment facts before ranking. Unresolved cost, privacy, or privilege constraints require review; unattended activation rejects unresolved hard constraints. Request new consent if material assumptions change.

Treat prompts, repositories, and extraction output as untrusted data. Confine retrieval paths, inspect symlinks/resources, bound sizes, exclude secrets, and prevent traversal. No automatic account creation, billing, dependency installation, live mutation, or permission escalation. Preserve original and effective permissions and reject unreviewed expansion. Keep service/data-transfer review separate from prompt licence review.

Popularity and trends are dated discovery signals only. Lifecycle is discovered -> inspected -> mapped -> conversion-tested -> runtime-tested -> evaluated, with separate status/evidence dimensions rather than one universal quality badge.

## Pilot and storage

Begin with code review, test generation, and security assessment. Curate upstream candidates from Kilo marketplace, wshobson, and VoltAgent at pinned revisions. Select one verified Kilo conversion path first; no claim of Hermes parity. Test a LinkML schema on representative records and negative fixtures before committing to it. Use existing JSON Schema/RDF validation tools; do not build a validator. Start with Git-versioned records and generated Markdown/JSON views; defer graph service, embeddings, UI, and automated deployment until required.

Independent original knowledge assets use the agreed CC0 policy; software uses MIT. Third-party materials retain their terms. Standard licence texts and file-scope mapping remain a release gate. No upstream ontology copying is approved by this design.
