# MedSync2

MedSync2 includes an Azure Essentials operationalization package for turning cloud-adoption research into GitHub-trackable work.

## Repository guidance

- [`AGENTS.md`](AGENTS.md): coding-agent and contributor guidance, including NEH Texas PMP policy guardrails.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): contributor workflow, compliance obligations, and PR process.
- [`SECURITY.md`](SECURITY.md): vulnerability reporting policy.
- [`CODEOWNERS`](CODEOWNERS): code ownership and required reviewers.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md): Copilot and Codex compliance instructions.
- [`docs/azure-essentials-operationalization.md`](docs/azure-essentials-operationalization.md): source boundary, operating model, official-resource index, and implementation gates.
- [`docs/cloud-adoption-backlog.md`](docs/cloud-adoption-backlog.md): P0/P1/P2 backlog for issues and pull requests.
- [`docs/cloud-adoption-dashboard.md`](docs/cloud-adoption-dashboard.md): current status of all backlog items, risks, and production-readiness blockers.
- [`docs/executive-brief.md`](docs/executive-brief.md): executive summary of MedSync2 cloud adoption status and open decisions.
- [`docs/architecture/azure-landing-zone-decision-record.md`](docs/architecture/azure-landing-zone-decision-record.md): landing-zone topology decision record.
- [`docs/architecture/identity-and-access-decision-record.md`](docs/architecture/identity-and-access-decision-record.md): identity and access model decision record.
- [`docs/architecture/data-protection-decision-record.md`](docs/architecture/data-protection-decision-record.md): data protection, PHI handling, and compliance evidence decision record.
- [`.github/ISSUE_TEMPLATE/azure-essentials-task.md`](.github/ISSUE_TEMPLATE/azure-essentials-task.md): issue template for Azure Essentials-aligned work.
- [`.github/ISSUE_TEMPLATE/data-model-task.md`](.github/ISSUE_TEMPLATE/data-model-task.md): issue template for data model and schema changes.
- [`.github/ISSUE_TEMPLATE/vendor-mapping-task.md`](.github/ISSUE_TEMPLATE/vendor-mapping-task.md): issue template for vendor field mapping and integration work.
- [`.github/ISSUE_TEMPLATE/dashboard-metric-task.md`](.github/ISSUE_TEMPLATE/dashboard-metric-task.md): issue template for dashboard metrics and KPI work.
- [`.github/ISSUE_TEMPLATE/compliance-review-task.md`](.github/ISSUE_TEMPLATE/compliance-review-task.md): issue template for compliance review requests.
- [`.github/pull_request_template.md`](.github/pull_request_template.md): pull request checklist including compliance-sensitive items.

## Operating model

1. **Readiness and foundation**: identity, environments, landing zone, cost baseline, repository controls, and data assumptions.
2. **Design and govern**: architecture, policy, review gates, AI guardrails, and deployment decisions.
3. **Manage and optimize**: observability, reliability, backup and restore, cost review, and ongoing remediation.

## Boundary

Azure Essentials material should guide MedSync2 execution, but final implementation decisions should be validated against current Microsoft documentation, the actual MedSync2 codebase, and product requirements.
