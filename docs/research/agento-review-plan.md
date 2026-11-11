# AgentO assessment plan

Status: pending source/artifact review; project landing page inspected 11 November 2026.

## Sources

- Project: https://agentic-patterns.github.io/
- Repository linked by project: https://github.com/agentic-patterns/agentic-ai-onto
- Ontology: https://w3id.org/agentic-ai/onto
- Archive: https://doi.org/10.5281/zenodo.18342624

## Preliminary evidence

The landing page describes an OWL/RDF ontology building on PROV-O, P-Plan, and BEAM, with concepts including teams, agents, capabilities, tasks, goals, workflow patterns, tools, resources, prompts, configuration, environments, and constraints. It reports a graph of 66 framework-derived workflow patterns and advertises CC-BY-4.0. These are project claims, not independently reproduced findings.

## Questions to answer before building

1. Pin a release or commit and inspect actual RDF/OWL, namespace stability, licence files, examples, tests, and maintenance evidence.
2. Distinguish abstract role contracts, reusable definitions, deployments, and executions: what does AgentO model already?
3. Check support for upstream repositories, paths, revisions, digests, licences, supporting resources, and conversion provenance.
4. Check dependencies, proprietary services, costs, data transfer, environment assumptions, privileges, and explicit unknowns.
5. Check task-to-role discovery, team composition, input/output contracts, independence of assurance, and selection explanations.
6. Separate declared capabilities, inferred mappings, compatibility tests, and observed task performance.
7. Inspect extraction quality, manual validation scope, and query examples; do not equate pattern count with routing effectiveness.
8. Assess alignment with SKOS, PROV-O, LinkML, A2A, and existing converters without assuming interchangeable semantics.
9. Determine legal boundaries for referencing, importing, extending, or copying CC-BY artifacts alongside original CC0 assets.

## Required output

Produce a source-cited fit/gap matrix: requirement, exact term or evidence, fit (native/partial/absent/unknown), extension needed, and licence implications. Recommend one of reuse unchanged, extend with a small complementary vocabulary, align independently, or reject with reasons. Do not build an overlapping ontology before this assessment.
