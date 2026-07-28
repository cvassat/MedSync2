# MedSync2 Coding-Agent Guidance

This repository uses the Azure Essentials operationalization package as a planning and implementation guardrail for MedSync2 cloud, AI, security, resiliency, and GitHub workflow work.

## Source-boundary rules

When working from Azure Essentials material, keep these categories separate:

1. **Source-derived Azure points**: concepts directly traceable to the Azure Essentials resource kit or the Azure Essentials update research supplied for this repository.
2. **Current Microsoft documentation**: current product names, navigation, pricing model descriptions, compliance references, and official implementation docs that must be verified against Microsoft sources at time of use.
3. **MedSync2-specific implementation decisions**: design choices made for this repository after reviewing its actual code, product requirements, regulated-data posture, and deployment target.
4. **General cloud-market analysis**: neutral context, including Azure-vs-AWS comparisons, that should never be represented as a Microsoft source claim.

Do not imply that the Azure Essentials source deck directly compares Azure and AWS. It does not.

## Current terminology baseline

Use current Microsoft terminology unless a legacy name is needed for searchability:

- Microsoft Foundry, formerly Azure AI Foundry.
- Microsoft Entra ID, formerly Azure Active Directory or Azure AD.
- Azure Proactive Resiliency Library v2 when referencing APRL implementation guidance.
- Azure Well-Architected Framework when evaluating workload readiness.
- Azure Monitor Baseline Alerts when standardizing Azure alerting baselines.
- Azure Verified Modules when evaluating reusable Bicep or Terraform modules.

## MedSync2 implementation guardrails

Before adding cloud infrastructure, AI, compliance, or deployment code:

1. Create or update a decision record in `docs/architecture/` if the change affects identity, tenancy, network topology, data residency, deployment topology, AI model behavior, protected data flow, or monitoring.
2. Link the work to `docs/cloud-adoption-backlog.md` or create a new GitHub issue using the Azure Essentials task template.
3. Validate the change against the operating model in `docs/azure-essentials-operationalization.md`.
4. Prefer GitHub issues and small pull requests over large untracked changes.
5. Use hyphenated filenames for new docs and deliverables. Keep GitHub-reserved paths such as `.github/ISSUE_TEMPLATE` when required by GitHub.
6. Do not add claims of HIPAA, HITRUST, SOC 2, FedRAMP, or other compliance achievement without verified scope, evidence, and owner approval.
7. Do not hard-code secrets, tenant IDs, subscription IDs, patient identifiers, API keys, or environment-specific credentials.

## Pull request checklist

Every cloud, AI, governance, or documentation PR should answer:

- What MedSync2 capability does this enable?
- Is the change source-derived, current-doc verified, or MedSync2-specific?
- Which Azure Essentials lifecycle stage does it support: readiness and foundation, design and govern, or manage and optimize?
- What security, cost, reliability, and compliance assumptions are introduced?
- What remains unverified or environment-specific?

## Compliance and PHI guardrails

These rules apply to every agent, Codex task, and human contributor. Violating any of them is a blocking issue.

### Hard rules — never do these

1. **Never encode independent outpatient PMHNP Schedule II signing authority.** Texas PMP policy requires collaborative practice agreement oversight for Schedule II controlled substances by PMHNPs in outpatient settings. Any logic that grants or implies standalone Schedule II prescribing authority for outpatient PMHNPs must not be committed.
2. **Never count a score-only PDMP workflow as a full report review by default.** Retrieving or displaying a risk score alone does not satisfy the full PDMP report-review requirement. Any workflow step modelling PDMP compliance must distinguish between score-only retrieval and full report review.
3. **Never expose raw patient identifiers in dashboard marts.** Analytics views, reporting marts, and dashboard queries must use de-identified or tokenized references. Direct patient identifiers (MRN, name, DOB, SSN, contact info) must not appear in mart tables or exported query results.

### General compliance rules

- **No PHI in the repository.** Do not commit, log, or embed protected health information in source code, configuration files, test fixtures, documentation, or comments. Use synthetic data or clearly labelled placeholder tokens in tests and examples.
- **No invented policy rules.** Do not encode a regulatory interpretation, clinical workflow rule, or compliance requirement that is not explicitly sourced from a cited policy document, vendor specification, or owner-approved decision record. If the authoritative source is unknown, use a `TODO` comment instead.
- **TODOs instead of assumptions.** When a source document, vendor field mapping, clinical rule, or regulatory citation is unknown at implementation time, insert a `TODO(compliance):` comment that describes exactly what must be resolved before the code can be considered production-ready. Do not guess or fill in plausible-sounding values.
- **Small, reviewable pull requests.** Break work into PRs that can be reviewed in a single sitting. PRs that touch compliance logic, data model fields, or PDMP/PMP workflow must not exceed 400 changed lines without owner approval.
- **Compliance reviewer signoff for policy logic.** Any PR that adds or modifies clinical decision rules, PDMP query logic, prescribing authority checks, or de-identification logic must include a signoff comment from a designated compliance reviewer before merge. Tag the reviewer in the PR description using the label `compliance-review`.
- **Source-boundary documentation required.** Every compliance-relevant decision must be traceable to one of the four source-boundary categories defined in the *Source-boundary rules* section above. State the category explicitly in the PR description or decision record.

## Recommended docs to keep current

- `README.md`: concise repository orientation and links.
- `docs/azure-essentials-operationalization.md`: operating model and source boundary.
- `docs/cloud-adoption-backlog.md`: prioritized execution queue.
- `docs/architecture/`: decision records for durable architecture choices.
