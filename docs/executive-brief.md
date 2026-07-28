# MedSync2 Executive Brief

Date: 2026-07-28

Audience: product owner, technical lead, security and compliance stakeholder

## What is MedSync2?

MedSync2 is a medication synchronization tool that calculates when and how much of each medication a patient needs to align refill dates. It is currently a pre-production Streamlit application targeting pharmacists and care-coordination workflows.

## Why the Azure Essentials framework matters for MedSync2

MedSync2 operates in a regulated healthcare context. Any path toward production deployment must address:

1. **HIPAA compliance** — medication records, patient identifiers, and dispenser data are Protected Health Information (PHI). Unauthorized access, disclosure, or inadequate safeguards carry civil and criminal liability.
2. **Texas PMP requirements** — prescribers accessing or recording PDMP data must do so through authenticated, auditable workflows. Score-only access does not satisfy a full-report review obligation.
3. **DEA scheduling rules** — any logic that encodes prescribing authority, controlled-substance scheduling, or PDMP compliance thresholds must be verified against current federal and Texas regulations before implementation.

The Azure Essentials framework provides MedSync2 with a structured path to address these requirements through cloud adoption lifecycle stages: readiness and foundation, design and govern, and manage and optimize.

## What has been done [MedSync2 decision]

| Deliverable | File | Purpose |
|---|---|---|
| Coding-agent guardrails | `AGENTS.md` | Hard constraints for every contributor, agent, and Codex task |
| Copilot generation defaults | `.github/copilot-instructions.md` | Inline guardrails for AI-assisted code generation |
| Compliance PR template | `.github/pull_request_template.md` | Gated checklist for compliance-sensitive changes |
| Issue templates | `.github/ISSUE_TEMPLATE/` | Codex-ready templates for data model, vendor mapping, dashboard, and compliance review work |
| Azure landing-zone decision record | `docs/architecture/azure-landing-zone-decision-record.md` | Defines decisions required before cloud deployment |
| Identity and access decision record | `docs/architecture/identity-and-access-decision-record.md` | Defines identity model, authentication, and audit requirements |
| Data protection decision record | `docs/architecture/data-protection-decision-record.md` | Defines PHI classification, de-identification, encryption, and compliance evidence requirements |
| Cloud adoption backlog | `docs/cloud-adoption-backlog.md` | Prioritized P0/P1/P2 execution queue |
| Cloud adoption dashboard | `docs/cloud-adoption-dashboard.md` | Current status of all backlog items and open risks |

## What is source-derived vs. MedSync2-specific

| Claim | Source | Type |
|---|---|---|
| Azure landing-zone lifecycle model | [Azure Essentials] | Source-derived |
| Azure Essentials P0/P1/P2 priority model | [Azure Essentials] | Source-derived |
| Microsoft Entra ID as Azure-native IdP | [MSFT docs: https://learn.microsoft.com/en-us/entra/fundamentals/new-name] | Current Microsoft documentation |
| Azure Monitor Baseline Alerts | [MSFT docs: https://azure.github.io/azure-monitor-baseline-alerts/] | Current Microsoft documentation |
| Azure Verified Modules | [MSFT docs: https://azure.github.io/Azure-Verified-Modules/] | Current Microsoft documentation |
| PDMP full-report vs. score-only distinction | [MedSync2 decision] | MedSync2-specific; grounded in Texas PMP policy |
| PMHNP Schedule II prohibition | [MedSync2 decision] | MedSync2-specific; requires Texas statutory verification |
| PHI annotation convention (`# PHI:`) | [MedSync2 decision] | MedSync2-specific coding convention |

## What decisions remain open

The following decisions must be made before production deployment. Each has a corresponding decision record or `TODO(compliance):` entry:

1. **Azure tenant, subscription, and environment topology** — no cloud infrastructure exists yet. (`azure-landing-zone-decision-record.md`)
2. **Prescriber and PDMP authentication model** — Texas PMP and AWARxE/PMP InterConnect credential requirements are not yet verified. (`identity-and-access-decision-record.md`)
3. **HIPAA Business Associate Agreement with Microsoft Azure** — must be obtained and documented before PHI is processed. (`data-protection-decision-record.md`)
4. **PDMP data retention requirements** — Texas Health & Safety Code §481.076 retention obligations not yet confirmed. (`data-protection-decision-record.md`)
5. **Breach notification procedure** — HIPAA 45 CFR §164.404 60-day notification requirement not yet implemented. (`data-protection-decision-record.md`)
6. **Deployment runtime** — Azure App Service, Container Apps, or other runtime not yet selected. (P1-1)
7. **Cost model** — Azure pricing assumptions not yet documented. (P1-3)

## Recommended next steps

| Priority | Action | Owner |
|---|---|---|
| P0 | Assign owners to all open decision records | Product owner |
| P0 | Obtain HIPAA BAA from Microsoft for Azure | Compliance owner |
| P0 | Verify Texas PMP/PDMP authentication requirements | Compliance owner |
| P0 | Resolve `TODO(compliance):` items in data-protection and identity records | Compliance owner + technical lead |
| P1 | Select Azure deployment runtime and create deployment topology record | Technical lead |
| P1 | Define SLOs and observability baseline | Technical lead |
| P1 | Document cost model and budget thresholds | Product owner + technical lead |
| P2 | Select IaC tooling (Bicep or Terraform) and scaffold `infra/` | Technical lead |
