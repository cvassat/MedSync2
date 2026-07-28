# Contributing to MedSync2

Thank you for contributing to MedSync2. This guide covers process expectations, compliance obligations, and source-boundary rules that apply to every contributor, human or automated.

## Before you start

Read the following before opening a pull request or issue:

- [`AGENTS.md`](AGENTS.md): hard constraints for agents, Copilot, and contributors, including NEH Texas PMP policy guardrails.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md): Copilot and Codex generation defaults.
- [`docs/azure-essentials-operationalization.md`](docs/azure-essentials-operationalization.md): source-boundary rules and operating model.

## Issues

Use the appropriate issue template from [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/):

| Template | When to use |
|---|---|
| `azure-essentials-task.md` | Cloud, AI, governance, or infrastructure work |
| `data-model-task.md` | Schema, mart, or data-layer changes |
| `vendor-mapping-task.md` | Vendor field mapping or integration work |
| `dashboard-metric-task.md` | Metrics, KPIs, or dashboard changes |
| `compliance-review-task.md` | Formal compliance review request |

## Pull requests

1. **Keep PRs small and focused.** One concern per PR. Do not mix policy logic, data model changes, and infrastructure changes.
2. **Use the PR template.** Fill in every section of [`.github/pull-request-template.md`](.github/pull-request-template.md).
3. **Compliance-sensitive PRs require a compliance reviewer.** Any PR that touches PMP workflow logic, PDMP integration, prescribing authority rules, controlled-substance scheduling, or patient-identifier handling must:
   - Add a compliance owner as a reviewer.
   - Be labeled `compliance-review-required`.
   - Not be merged without explicit compliance reviewer approval.
4. **No PHI in the repository.** Never commit real patient names, MRNs, dates of birth, SSNs, diagnoses, or any other Protected Health Information. Use synthetic data in all examples, tests, and fixtures.
5. **TODOs over silent assumptions.** When a policy rule, vendor field, or source mapping is unknown, add a `TODO(compliance):`, `TODO(vendor):`, or `TODO(source):` comment and open a follow-up issue. Do not guess.
6. **No hard-coded secrets.** Never commit API keys, tokens, credentials, tenant IDs, subscription IDs, or patient identifiers. Use environment variables, Azure Key Vault references, or `# TODO: load from Key Vault` placeholders.

## Code style

- Match the existing style of the file you are editing.
- Prefer explicit, readable conditionals over compressed ternary chains for clinical or regulatory logic.
- Add docstrings to any function that encodes a policy rule, citing the governing statute or policy document.

## Source-boundary labeling

When comments or documentation reference external standards, label the source:

- `[Azure Essentials]` — derived from the Azure Essentials resource kit.
- `[MSFT docs: <URL>]` — verified against current Microsoft documentation.
- `[MedSync2 decision]` — a MedSync2-specific design decision.

## Architecture decision records

Create or update a decision record in `docs/architecture/` for any change that affects:

- Identity, tenancy, or access control
- Network topology or data residency
- Deployment topology or environment structure
- AI model behavior or prompt/response handling
- Protected data flow or audit logging
- Monitoring or observability baseline

## Getting help

Open a GitHub issue using the appropriate template, or start a discussion. Do not include PHI or credentials in any issue, discussion, or comment.
