# MedSync2 Coding-Agent Guidance

This repository uses the Azure Essentials operationalization package as a planning and implementation guardrail for MedSync2 cloud, AI, security, resiliency, and GitHub workflow work.

## NEH Texas PMP policy guardrails

The following rules are **hard constraints** that apply to every agent, Codex task, Copilot suggestion, and human contribution. Violations require a mandatory compliance reviewer signoff before merge.

### Absolute prohibitions

1. **Never encode independent outpatient PMHNP Schedule II signing authority.** Do not write code, configuration, logic, or documentation that grants a psychiatric-mental-health nurse practitioner independent authority to prescribe or sign Schedule II controlled substances in an outpatient setting under Texas law unless a verified, current Texas statutory or regulatory citation is supplied and reviewed by a compliance owner.
2. **Never count a score-only PDMP workflow as a full report review by default.** Accessing a risk score or summary does not satisfy the Texas PDMP full-report review requirement. Any workflow that records PDMP compliance must distinguish between score-only access and full-report review. Do not conflate the two without an explicit, reviewed policy decision.
3. **Never expose raw patient identifiers in dashboard marts or reporting layers.** Patient names, MRNs, dates of birth, SSNs, and other direct identifiers must be removed or tokenized before data reaches any analytics mart, dashboard query, or reporting export. Use surrogate keys or de-identification functions; never pass raw PHI through mart or dashboard layers.

### PHI and sensitive data rules

- **No PHI in the repository.** Do not commit real patient names, MRNs, dates of birth, addresses, diagnoses, medication records, insurance identifiers, or any other Protected Health Information to source code, configuration files, tests, fixtures, or documentation.
- Use synthetic or clearly labeled fake data for all examples, tests, and fixtures.
- If a field name or schema column could hold PHI, annotate it with a `# PHI: <description>` comment and document the de-identification or access-control mechanism in the relevant architecture decision record.

### No invented policy rules

- Do not invent, assume, or extrapolate Texas PMP, DEA, or HIPAA policy rules from general knowledge. If the exact policy text is not available in the repository or linked reference, add a `TODO(compliance): verify <rule description>` comment and open a compliance review issue before implementing the logic.
- Do not add compliance claims (HIPAA, HITRUST, SOC 2, FedRAMP, PDMP) without verified scope, evidence, and owner approval.

### TODOs over assumptions

- When a source field, vendor field, policy rule, or data mapping is unknown or unverified, add a `TODO(source): <description of what needs verification>` comment rather than making an assumption.
- Mark every unverified vendor-specific field with `TODO(vendor): confirm field name and semantics with <vendor name>`.
- Do not silently default to a value that may carry clinical or legal significance. Make the assumption visible.

### Small PRs and compliance reviewer signoff

- Keep pull requests small and focused on a single concern. Avoid mixing policy logic, data model changes, and infrastructure changes in one PR.
- Any PR that touches PMP workflow logic, PDMP integration, prescribing authority rules, controlled-substance scheduling, or patient-identifier handling **must** include a compliance reviewer in the reviewers list and must not be merged without their approval.
- Add `compliance-review-required` as a label on any such PR.

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
- Does this PR touch PMP workflow, PDMP integration, prescribing authority, or patient identifiers? If yes, is a compliance reviewer assigned?

## Recommended docs to keep current

- `README.md`: concise repository orientation and links.
- `docs/azure-essentials-operationalization.md`: operating model and source boundary.
- `docs/cloud-adoption-backlog.md`: prioritized execution queue.
- `docs/architecture/`: decision records for durable architecture choices.
