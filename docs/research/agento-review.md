# AgentO preliminary review

Reviewed: 11 November 2026. Status: preliminary source review; not a complete audit or executed validation.

## Scope and provenance

GitHub history and ontology.ttl were inspected through the GitHub connector during the project-design session. The default-branch head reported was e99a6e7cd7629210f6d4e2309d03a1cd9db8713f. The ontology file returned Git blob SHA c7cc659ecc99085e381a4ba3eeb6fbb828c95a5f and owl:versionInfo 1.1. The file was requested from the default branch, not explicitly pinned during retrieval; use the head-linked reference below to reproduce and verify it. Landing-page claims and source findings are distinguished below. No ontology reasoner, resolver, extraction pipeline, or benchmark was executed.

Sources:
- Repository: https://github.com/agentic-patterns/agentic-ai-onto
- History: https://github.com/agentic-patterns/agentic-ai-onto/commits/
- Observed head: https://github.com/agentic-patterns/agentic-ai-onto/commit/e99a6e7cd7629210f6d4e2309d03a1cd9db8713f
- Ontology at observed head: https://github.com/agentic-patterns/agentic-ai-onto/blob/e99a6e7cd7629210f6d4e2309d03a1cd9db8713f/ontology.ttl
- Landing page: https://agentic-patterns.github.io/
- Archived deposit: https://doi.org/10.5281/zenodo.18342624

## Maintenance evidence

The default-branch history returned twelve commits: eleven from May 2025 and one on 5 December 2025. Latest: e99a6e7, author/committer timestamp 2025-12-05T11:33:00Z, message 'update extractor'. Previous: d18beea, 26 May 2025, 'update title'; preceding ontology update: 1125220, 26 May 2025, 'update onto'. No later commits appeared in that returned history. This supports limited visible default-branch maintenance, not a claim that the project is abandoned or that no work exists elsewhere. The landing page identifies an ESWC 2026 artifact; publication year is not evidence of recent code changes.

## Verified Zenodo metadata

The DOI resolves to 'AgentO: An Ontology for Modeling Agentic AI Systems', published 22 January 2026, version v1, classified as a data paper. It lists one downloadable file, agento.zip, size 7.6 kB, MD5 c753ef8581fbc9d480c6188f8125e9c3. These values were read from the deposit page. The archive was NOT downloaded, unpacked, compared with GitHub, or runtime-tested. The published checksum was not independently calculated. Do not conflate deposit version v1 with ontology owl:versionInfo 1.1 or infer they describe different content. A Zenodo publication date alone does not establish when archive contents were authored.

## Findings from ontology.ttl

1. Roles are represented by agentRole, an owl:DatatypeProperty from Agent to xsd:string, rather than a first-class role concept in the inspected file. This is inadequate by itself for our canonical role contracts, hierarchy, aliases, and implementation mappings.
2. Useful relationships include Task/requiresCapability/Capability, Agent/hasCapability/Capability, Team/hasAgentMember/Agent, Team/hasWorkflowPattern/WorkflowPattern, Agent/operatesIn/Environment, Task/requiresResource/Resource, and Agent/usesTool/Tool.
3. The inspected file does not declare LLMAgent, HumanAgent, Prompt, or Config, although the landing page describes them. It contains no owl:imports declarations or explicit PROV-O, P-Plan, or BEAM alignments. This is a version/artifact discrepancy to investigate, not proof that every AgentO artifact lacks them.
4. ExecutionStep and WorkflowStep are separate classes without an explicit relationship in the inspected file. hasAssociatedTask and stepOrder use ExecutionStep; nextStep and performedBy use WorkflowStep. This could impede consistent querying; no reasoner-based defect has been demonstrated.
5. The ontology is generic rather than tied to a vendor, but generic Agent/Tool/Resource/Environment classes do not provide a detailed implementation dependency or deployment-policy contract.

## Reported research claims, not reproduced

The landing page reports 66 framework-derived workflow patterns and 24 manually verified patterns, and describes reuse of PROV-O, P-Plan, and BEAM. These are author-reported claims. Extraction quality, coverage, and routing effectiveness were not independently assessed.

## Preliminary fit/gap matrix

| Requirement | Fit | Evidence or limitation |
|---|---|---|
| General agents, tasks, teams, tools | Partial/native conceptual overlap | Explicit classes and properties in ontology.ttl |
| Workflow representation | Partial | Patterns and steps exist; step-class usage needs review |
| First-class canonical role contracts | Absent in inspected file | agentRole is a string-valued property |
| Role specialisation and semantic mappings | Not found in inspected file | No corresponding structured role vocabulary observed |
| Upstream prompt implementation registry | Not found in inspected file | Repository/path/revision/converter records not modelled explicitly |
| Content digests and conversion provenance | Not found in inspected file | Needs separate registry/provenance design |
| Proprietary services, costs, environment assumptions | Partial generic overlap | Resource/environment concepts exist, detailed disclosures not found |
| Declared versus evaluated capabilities | Not found in inspected file | hasCapability does not encode this evidence distinction |
| Policy-constrained discovery and deployment | Not demonstrated | No end-to-end resolver inspected or tested |

'Not found' applies to the inspected Turtle file, not the entire repository or Zenodo archive. Standard external vocabularies may supply some missing metadata; do not invent replacements without checking.

## Licensing discrepancy

The repository README states MIT, while the landing page advertises CC-BY-4.0 and ontology.ttl rights metadata points to http://creativecommons.org/licenses/by/4.0/. Exact per-artifact licensing remains unresolved. Do not assume the README relicenses ontology content or that source availability permits CC0 redistribution. Our CC0 knowledge assets must not silently absorb third-party attribution obligations. Reference, align, or separately attribute material as appropriate after reviewing the actual terms; this is not legal clearance.

## Preliminary recommendation

Treat AgentO as a reference and potential alignment target, not an adopted hard dependency or wholesale ontology foundation. Our emphasis is task-to-role discovery, role contracts, upstream implementation selection, explicit assumptions, and reproducible policy-aware deployment. AgentO provides useful system/workflow concepts but the inspected artifact does not establish those discovery/registry functions. This recommendation is provisional pending archived-artifact inspection.

## Next evidence tasks

1. Retrieve agento.zip from the DOI record, independently verify its published checksum, list its files, and calculate SHA-256 digests. Do not execute archive contents.
2. Compare archived ontology terms, metadata, licence texts, examples, and mappings with the observed GitHub revision.
3. Inspect the website source or documented release references to identify which ontology version its descriptions concern.
4. Review extraction examples, query examples, validation evidence, and external vocabulary alignments.
5. Resolve licence scope or seek maintainer clarification before copying definitions.
6. Update the fit/gap matrix, then decide reuse, minimal extension, independent alignment, or rejection. No overlapping ontology implementation is authorised merely by this review.
