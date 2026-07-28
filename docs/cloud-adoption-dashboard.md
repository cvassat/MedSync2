# MedSync2 Cloud Adoption Dashboard

Last updated: 2026-07-28

This dashboard summarizes the status of every Azure Essentials backlog item, open decision records, risks, and production-readiness blockers.

## P0: Repository and governance foundation

| Item | Output | Status | Blocker |
|---|---|---|---|
| P0-1: Source-boundary and coding-agent rules | `AGENTS.md`, `.github/copilot-instructions.md`, issue templates, PR template | ✅ Complete | — |
| P0-2: Azure landing-zone decision record | `docs/architecture/azure-landing-zone-decision-record.md` | 🟡 Draft | Tenant, subscription, region decisions pending |
| P0-3: Identity and access decision record | `docs/architecture/identity-and-access-decision-record.md` | 🟡 Draft | Prescriber auth and PDMP auth requirements unverified |
| P0-4: Data protection and compliance evidence | `docs/architecture/data-protection-decision-record.md` | 🟡 Draft | HIPAA BAA, PDMP retention, breach notification pending |

## P1: Implementation enablement

| Item | Output | Status | Blocker |
|---|---|---|---|
| P1-1: Deployment topology | `docs/architecture/deployment-topology.md` | 🔴 Not started | P0-2 landing-zone decision required first |
| P1-2: Observability and resiliency baseline | `docs/architecture/observability-decision-record.md` | 🔴 Not started | P1-1 deployment topology required first |
| P1-3: Cost-management and FinOps plan | `docs/architecture/cost-management-plan.md` | 🔴 Not started | P0-2 landing-zone and P1-1 topology required first |
| P1-4: AI/agent decision gate | `docs/architecture/ai-agent-decision-record.md` | 🔴 Not started | Needed only if AI functionality is pursued |

## P2: Hardening and optimization

| Item | Output | Status | Blocker |
|---|---|---|---|
| P2-1: Infrastructure-as-code standards | `infra/` (Bicep or Terraform) | 🔴 Not started | P1-1 deployment topology required first |
| P2-2: Cloud adoption dashboard | `docs/cloud-adoption-dashboard.md` | ✅ This document | — |
| P2-3: Executive brief | `docs/executive-brief.md` | ✅ Complete | — |

## Architecture decision records

| Record | Status | Next action |
|---|---|---|
| `azure-landing-zone-decision-record.md` | 🟡 Draft — options defined | Assign owner; select topology |
| `identity-and-access-decision-record.md` | 🟡 Draft — constraints defined | Resolve `TODO(compliance):` items; assign owner |
| `data-protection-decision-record.md` | 🟡 Draft — constraints defined | Obtain HIPAA BAA; resolve retention TODOs; assign owner |
| `deployment-topology.md` | 🔴 Not created | Create after P0-2 decisions |
| `observability-decision-record.md` | 🔴 Not created | Create after P1-1 |
| `cost-management-plan.md` | 🔴 Not created | Create after P0-2 and P1-1 |
| `ai-agent-decision-record.md` | 🔴 Not created | Create only if AI functionality is planned |

## Open risks

| Risk | Severity | Owner | Status |
|---|---|---|---|
| No HIPAA BAA documented with Azure/Microsoft | High | To be assigned | Open |
| PDMP full-report vs. score-only conflation possible without explicit guards | High | To be assigned | Mitigated in AGENTS.md; enforcement in code TBD |
| No prescriber identity verification flow implemented | High | To be assigned | `TODO(compliance):` filed in identity-and-access record |
| No audit log for PHI access | High | To be assigned | Open |
| Raw patient identifiers could appear in application logs | Medium | To be assigned | `TODO(compliance):` filed; no PHI log policy enforced yet |
| No breach notification procedure | High | To be assigned | `TODO(compliance):` filed in data-protection record |
| No production environment or deployment topology | Medium | To be assigned | P1-1 not started |
| No secret rotation policy | Medium | To be assigned | Open |

## Production-readiness blockers

The following must be resolved before any production deployment:

- [ ] Azure landing-zone topology selected (`docs/architecture/azure-landing-zone-decision-record.md` finalized)
- [ ] Identity and access model finalized, including prescriber and PDMP auth (`docs/architecture/identity-and-access-decision-record.md`)
- [ ] HIPAA BAA obtained and documented
- [ ] PDMP data-handling requirements verified under Texas Health & Safety Code §481.076
- [ ] PHI audit log implemented and tested
- [ ] No hard-coded credentials in any deployment path
- [ ] All `TODO(compliance):` items in data-protection and identity records resolved or explicitly deferred with owner approval
- [ ] Breach notification procedure documented

## Review cadence

Update this dashboard when:
- A backlog item status changes.
- A new risk is identified.
- A decision record is finalized.
- A production-readiness blocker is resolved or added.
