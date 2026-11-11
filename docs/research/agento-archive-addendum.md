# AgentO archive review addendum

Date: 11 November 2026. Supplements agento-review.md; preserves the earlier GitHub-only findings.

## Evidence and limits

The user supplied three files extracted from the Zenodo archive: ontology.ttl (27,755 bytes), extractor/analysis.prompt.md (2,509 bytes), and extractor/run_prompt.py (2,918 bytes). Individual attachment hashes were calculated; original ZIP bytes and its published MD5 were not verified. These files are user-supplied archive contents, not an independently retrieved deposit. Python AST parsing succeeded; the extractor was not executed. RDFLib was unavailable, so no RDF parsing, reasoning, SHACL validation, or benchmark was completed.

SHA-256 of uploaded bytes:
- ontology.ttl: aa38576497aea5597f13808e208c227e4c39fa52adfd3cef715ab24fd966348e
- analysis.prompt.md: 4d54fd1bcfcf5f928a1790fd298937370a9a34faabc7214d3aace423427018ec
- run_prompt.py: 1b502b49f47eac0544ff44971a1ed1ff3e4045644b957929ed7fdcd54499d07d

## Corrections and expanded findings

The archive has owl:versionInfo 0.2, versus 1.1 in the previously inspected GitHub file. These labels do not establish chronology. The archive declares LLMAgent, HumanAgent, Prompt, and Config. LLMAgent subclasses prov:Agent and Tool; HumanAgent subclasses prov:Agent; WorkflowPattern subclasses p-plan:Plan; WorkflowStep subclasses p-plan:Step. BEAM vocabulary is referenced. Lack of owl:imports does not mean lack of alignment: explicit references and subclass axioms supply alignment without import declarations. The prior missing-class/alignment findings apply only to the GitHub file.

The archived hasAssociatedTask declaration uses WorkflowStep, unlike the earlier GitHub declaration using ExecutionStep. Do not carry the earlier step mismatch forward as an established archive defect. Other axioms still need formal validation. LLMAgent being a Tool is an explicit modelling choice, not a demonstrated contradiction.

Roles remain string-valued: agentRole has domain LLMAgent and range xsd:string. This does not provide our first-class canonical role contracts, specialisation, aliases, or implementation mappings. Richer system modelling is not evidence of a working registry/resolver. Earlier absence claims must not be generalised to the archive without inspecting the relevant terms.

## Extractor assumptions

run_prompt.py imports the OpenAI SDK and selects gpt-5-mini. It creates OpenAI() before setting OPENAI_API_KEY to an empty string; this is confusing credential handling, not a reliable setup instruction. It expects agentic-o.ttl rather than supplied ontology.ttl, and resolves prompt/ontology paths against the working directory. It walks src/ if present, otherwise the selected folder, reading files without an explicit secrets, binary, size, or dependency-directory exclusion policy. File contents are assembled into a model request. It writes returned text directly as TTL without RDF/schema validation. Do not execute it on a private workspace unchanged. These are implementation observations, not claims that using the ontology requires OpenAI.

analysis.prompt.md asks for framework-neutral reconstruction of an agent solution using a fixed schema, preserving prompts and parameters and reporting missing concepts in comments. Our goal differs: abstract role discovery and policy-constrained selection of upstream implementations, not full solution reconstruction.

## Revised recommendation

AgentO is a stronger system/workflow alignment candidate than its GitHub artifact suggested. Do not adopt it wholesale or dismiss it solely for low visible commit activity. Proceed with an independently authored, tool-neutral role/discovery contract and evaluate explicit crosswalks against the archived ontology. Do not assert equivalence where AgentO agents, our roles, definition artifacts, and deployments differ.

The ontology declares CC-BY-4.0 rights; repository README and website statements previously differed. Per-artifact terms remain unresolved. No upstream definitions are copied here. Original analysis is not legal clearance for imports, derivatives, or redistribution. Before any adoption: preserve a reproducible artifact, validate it with existing RDF tools, inspect licence scope, test concrete competency questions, and record the alignment decision.

References: https://doi.org/10.5281/zenodo.18342624 ; https://github.com/agentic-patterns/agentic-ai-onto ; https://agentic-patterns.github.io/
