# I01 — Read-only mechanical inventory

Worker: local Kilo. Requires explicit owner approval of read roots and private output directory. No ontology design or prompt execution.

Proposed read roots:
- ~/.config/kilo/agents
- ~/.agents/repos/agents
- ~/.agents/repos/awesome-claude-code-subagents
- ~/.local/share/kilo/repos/kilo-marketplace

Only the installed-agent root is enumerated. Repo roots are read only for Git revision/status; no whole-repository crawl. No network or package installation. Choose approved private output OUTSIDE agent discovery directories and tracked source. Outputs: files.jsonl, sources.json, report.md. Absolute paths stay private; public export is separate approval.

For Markdown regular files: relative path, kind=regular_file, size_bytes, raw-byte SHA-256, status=ok/read_error, nullable error. No normalization or frontmatter parsing. For every symlink encountered (any extension): relative path, kind=symlink, literal target, status=not_followed. Do not open targets or recurse symlink directories. Report unreadable directories. Other regular files are out of scope. Do not read devices, sockets, or FIFOs.

Use existing filesystem/hash/Git tools or an established inventory tool before custom code. If no existing tool safely produces these records, stop with a proposal rather than silently create a new application. No prompt-body hashes in I01.

Repo provenance: logical source ID, full HEAD if available, dirty boolean, errors. Do not collect credential-bearing remote URLs or full Git configuration. Missing provenance remains unknown. Do not infer file origin solely from its basename.

Example:
{"path":"wshobson/systems-programming/rust-pro.md","kind":"regular_file","size_bytes":1234,"sha256":"<actual 64 hexadecimal characters>","status":"ok","error":null}

Acceptance: path-sorted records; all in-scope files/errors accounted for; independently spot-check first/middle/last readable hashes with sha256sum; reconcile regular-file count against an independent non-following listing. Zero input changes. Return counts/private output location, not all data in chat. No prompt publication, push, rename, deduplication, classification, or semantic uniqueness claims. Use REPORT-TEMPLATE.md.
