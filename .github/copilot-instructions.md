# Copilot Instructions for MedSync2

These instructions apply to all GitHub Copilot suggestions, Copilot Chat responses, and Codex-powered tasks in this repository. They supplement and do not replace `AGENTS.md`.

## Compliance-first defaults

MedSync2 operates in a regulated healthcare context subject to Texas PMP law, DEA scheduling rules, and HIPAA. Apply the following defaults in every suggestion:

### Hard stops — never suggest the following without a verified citation and compliance owner approval

- **Do not** generate code or logic that grants an outpatient PMHNP independent Schedule II signing authority under Texas law. If the feature requires prescribing authority logic, insert `# TODO(compliance): verify PMHNP Schedule II authority under Texas Occ. Code and current DEA rules before implementing` and stop.
- **Do not** treat a PDMP score-only access as equivalent to a full PDMP report review. Use separate boolean flags or status codes for `pdmp_score_accessed` versus `pdmp_full_report_reviewed`. Do not collapse them into a single field without explicit policy documentation.
- **Do not** pass raw patient identifiers (name, MRN, DOB, SSN, address) through any mart, dashboard query, reporting layer, API response, or log line. Use surrogate keys or de-identified tokens at the boundary.

### PHI

- Never include real patient data in code, tests, fixtures, configuration, or documentation suggestions.
- When generating example data, use clearly synthetic values (`patient_id: "TEST-001"`, `mrn: "FAKE-MRN-12345"`).
- If a schema column or function parameter will hold PHI, add a `# PHI: <description>` comment in the suggestion.

### Policy logic

- Do not invent or extrapolate Texas PMP, PDMP, DEA, or HIPAA rules from general knowledge. If a rule is needed and its exact source is not in the current file or a linked reference, generate a `TODO(compliance): <description>` comment instead of a speculative implementation.
- Do not silently default boolean compliance flags to `True` or `False` when the correct default depends on unverified policy. Use `None` or raise a `NotImplementedError` with a descriptive message.

### TODOs over assumptions

- When a vendor field, data-source mapping, or integration parameter is unknown, generate `# TODO(vendor): confirm <field> with <vendor>` rather than guessing a value.
- When a source document is cited but not available in the repository, generate `# TODO(source): link or attach <document name>` rather than paraphrasing from memory.

## Code quality

- Keep suggested changes small and focused. If a change touches both policy logic and infrastructure, split the suggestion into separate steps and note the separation.
- Prefer explicit, readable conditionals over compressed ternary chains when the logic involves clinical or regulatory rules.
- Add docstrings to any function that encodes a policy rule, citing the governing statute or policy document in the docstring.

## Secrets and credentials

- Never suggest hard-coded secrets, API keys, tenant IDs, subscription IDs, or patient identifiers.
- Use environment variables, Azure Key Vault references, or placeholder comments (`# TODO: load from Key Vault`) for all sensitive values.

## Source-boundary labeling

When generating documentation or comments that reference external standards:

- Label Azure Essentials-derived points with `[Azure Essentials]`.
- Label Microsoft-doc-verified points with `[MSFT docs: <URL>]`.
- Label MedSync2-specific decisions with `[MedSync2 decision]`.
- Do not mix sources without labeling them.
