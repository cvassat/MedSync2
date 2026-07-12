# MedSync2 Cloud Adoption Backlog

This backlog converts the Azure Essentials update research into GitHub-trackable work for MedSync2. It is intentionally implementation-oriented: each item should become an issue, pull request, or decision record.

## Priority model

| Priority | Meaning |
|---|---|
| P0 | Required before cloud or AI implementation can be trusted. |
| P1 | High-value delivery work after P0 guardrails exist. |
| P2 | Optimization, hardening, and documentation depth. |

## P0: repository and governance foundation

### P0-1: Establish source-boundary and coding-agent rules

- Status: started in this branch.
- Files: `AGENTS.md`, `docs/azure-essentials-operationalization.md`.
- Definition of done:
  - Coding agents can distinguish source-derived Azure points, current Microsoft documentation, MedSync2 decisions, and general market analysis.
  - New files use hyphenated names except GitHub-reserved directories.
  - PRs identify lifecycle stage and assumptions.

### P0-2: Create Azure landing-zone decision record

- Output path: `docs/architecture/azure-landing-zone-decision-record.md`.
- Questions:
  - Which tenant and subscriptions will MedSync2 use?
  - Which regions are allowed?
  - What environments are required?
  - Which team owns platform controls?
  - What branch/environment protections map to deployments?
- Definition of done:
  - Tenant, subscriptions, environments, region assumptions, identity dependencies, and owners are documented.
  - Unknowns are explicitly marked.

### P0-3: Define identity and access model

- Output path: `docs/architecture/identity-and-access-decision-record.md`.
- Questions:
  - How will Microsoft Entra ID be used?
  - Which roles are human, service, automation, and break-glass?
  - Which GitHub secrets or OIDC federation paths are allowed?
- Definition of done:
  - No hard-coded credentials are required.
  - Least-privilege roles are stated.
  - Production access workflow is documented.

### P0-4: Define regulated-data and compliance evidence posture

- Output path: `docs/architecture/data-protection-decision-record.md`.
- Questions:
  - Does MedSync2 process PHI, PII, credentials, or protected operational logs?
  - What is the encryption, retention, access, and audit model?
  - Which compliance references are evidence sources versus aspirational controls?
- Definition of done:
  - The repository does not claim compliance certification without evidence.
  - Evidence owners and evidence locations are defined.

## P1: implementation enablement

### P1-1: Build MedSync2 deployment topology

- Output path: `docs/architecture/deployment-topology.md`.
- Candidate runtime options:
  - Azure App Service.
  - Azure Container Apps.
  - Azure Kubernetes Service only if operational complexity is justified.
- Definition of done:
  - Runtime is chosen with rationale.
  - Environment promotion path is documented.
  - Rollback and secret-management approach are documented.

### P1-2: Add observability and resiliency baseline

- Output path: `docs/architecture/observability-decision-record.md`.
- Inputs:
  - Azure Well-Architected Framework.
  - Azure Monitor Baseline Alerts.
  - Azure Proactive Resiliency Library v2.
- Definition of done:
  - Service-level objectives are stated.
  - Alerts, dashboards, logs, metrics, and traces are defined.
  - Backup and restore test expectations are documented.

### P1-3: Add cost-management and FinOps plan

- Output path: `docs/architecture/cost-management-plan.md`.
- Questions:
  - What are the expected monthly cost ranges by environment?
  - What budgets and alerts are required?
  - What deployment choices materially change cost?
- Definition of done:
  - Azure Pricing Calculator assumptions are documented.
  - Cost owners and review cadence are defined.

### P1-4: Gate AI or agent functionality

- Output path: `docs/architecture/ai-agent-decision-record.md` if AI is pursued.
- Required sections:
  - Approved use cases.
  - Excluded use cases.
  - Data classification.
  - Model and deployment mode.
  - Prompt and response retention.
  - Azure AI Content Safety or equivalent safety controls.
  - Evaluation and human-review workflow.
  - Cost model, including pay-per-token versus provisioned throughput when appropriate.
- Definition of done:
  - AI behavior is testable, observable, and bounded.
  - No autonomous clinical or compliance decision is introduced without explicit review.

## P2: hardening and optimization

### P2-1: Introduce infrastructure-as-code standards

- Candidate paths:
  - `infra/bicep/`.
  - `infra/terraform/`.
- Inputs:
  - Azure Verified Modules.
  - Repository deployment topology.
- Definition of done:
  - IaC language is selected.
  - Modules are pinned or versioned.
  - Security review checklist is added.

### P2-2: Add decision dashboard

- Output path: `docs/cloud-adoption-dashboard.md`.
- Include:
  - P0/P1/P2 status.
  - Decision records completed.
  - Open risks.
  - Production-readiness blockers.
  - Cost and reliability review cadence.

### P2-3: Add executive brief

- Output path: `docs/executive-brief.md`.
- Audience:
  - Product owner.
  - Technical lead.
  - Security/compliance stakeholder.
- Include:
  - Why the Azure Essentials framework matters for MedSync2.
  - What is source-derived versus MedSync2-specific.
  - What decisions remain open.

## Issue-ready task template

Use this structure when converting backlog items into GitHub issues:

```markdown
## Objective

## Azure Essentials lifecycle stage

- [ ] Readiness and foundation
- [ ] Design and govern
- [ ] Manage and optimize

## Source boundary

- [ ] Source-derived Azure point
- [ ] Current Microsoft documentation
- [ ] MedSync2-specific decision
- [ ] General market analysis

## Acceptance criteria

- [ ]
- [ ]
- [ ]

## Evidence and links

## Open assumptions
```
