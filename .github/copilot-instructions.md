# MedSync2 Copilot Instructions

This file provides inline guidance for GitHub Copilot and Copilot coding agent. The authoritative agent reference is `AGENTS.md` at the repository root. Read it before making any change. This file adds Copilot-specific emphasis.

## Quick-reference rules

1. **No PHI in the repository.** Do not generate, suggest, or commit protected health information in code, tests, config, docs, or comments. Use synthetic data or `TODO` placeholders.
2. **No invented policy rules.** Do not generate clinical workflow logic, prescribing authority checks, or regulatory compliance rules unless the source document is cited. Insert a `TODO(compliance): <what must be verified>` comment instead.
3. **TODOs for unknown vendor or source fields.** If a vendor API field, PDMP data element, or regulatory citation is not known, emit `TODO(vendor-mapping):` or `TODO(source-unknown):` rather than guessing a value.
4. **Small pull requests.** Keep PRs focused. PRs touching compliance logic, data models, or PDMP/PMP workflow must stay under 400 changed lines without explicit owner approval.
5. **Compliance reviewer signoff.** PRs that add or modify clinical decision rules, PDMP queries, prescribing authority checks, or de-identification logic require a `compliance-review` label and a designated reviewer comment before merge.

## Hard rules — never generate code that does the following

- Grants or implies standalone Schedule II prescribing authority for outpatient PMHNPs (Texas PMP policy requires collaborative practice agreement oversight).
- Treats a score-only PDMP retrieval as equivalent to a full PDMP report review.
- Includes raw patient identifiers (MRN, name, DOB, SSN, contact info) in dashboard mart queries or exported analytics.

## When in doubt

- Surface the ambiguity as a `TODO(compliance):` comment.
- Reference the relevant section of `AGENTS.md` or `docs/azure-essentials-operationalization.md`.
- Do not proceed with a plausible-sounding guess for compliance-sensitive logic.
