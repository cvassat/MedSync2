# Identity and Access Decision Record

Status: draft

Date: 2026-07-28

## Decision

MedSync2 has not yet finalized its identity and access model. This record defines the minimum decisions that must be made before any production or shared-environment deployment.

## Context

MedSync2 processes or will process medication synchronization workflows that may involve protected health information and regulated prescribing workflows. Identity and access controls must satisfy HIPAA minimum-necessary principles, Texas PMP requirements for authenticated prescriber access, and standard least-privilege practices for Azure-hosted workloads.

## Required decisions

| Area | Current answer | Owner | Status |
|---|---|---|---|
| Identity provider for human users | Microsoft Entra ID assumed for Azure-native identity | To be assigned | Draft assumption |
| Identity provider for service-to-service | Managed identities or workload identity federation preferred; no service passwords | To be assigned | Open |
| GitHub authentication to Azure | OIDC federation preferred over long-lived secrets | To be assigned | Open |
| Role definitions for human users | Developer, reviewer, compliance-owner, read-only operator, break-glass admin | To be assigned | Open |
| Role definitions for service principals | Per-workload least-privilege roles; no Owner or Contributor on production without approval | To be assigned | Open |
| Break-glass account policy | Required before production; access must be audited and time-limited | To be assigned | Open |
| Multi-factor authentication | Required for all interactive production access | To be assigned | Open |
| Prescriber identity verification | `TODO(compliance): verify Texas PMP prescriber identity requirements` | To be assigned | Open |
| PDMP access authentication | `TODO(compliance): verify AWARxE/PMP InterConnect authentication requirements` | To be assigned | Open |
| PHI data access roles | Read access to PHI-bearing stores must be scoped to clinical roles only; audit log required | To be assigned | Open |
| Session and token lifetime | To be determined based on HIPAA session-management guidance | To be assigned | Open |
| Privileged access workstations | To be determined | To be assigned | Open |

## Design constraints

1. **No hard-coded credentials.** No service password, API key, client secret, or patient identifier may appear in source code, configuration files, CI/CD pipeline definitions, or documentation.
2. **Least privilege.** Every identity (human, service, automation) receives only the permissions required for its specific function. Broad roles such as Owner or Contributor on production subscriptions require documented justification and time-limited assignment.
3. **Audit logging.** All access to PHI-bearing resources, PDMP integration endpoints, and PMP workflow systems must produce an audit log entry with identity, action, resource, and timestamp.
4. **Separation of duties.** The identity that deploys infrastructure must not also hold the keys to production patient data. Compliance reviewers must be distinct from the developers who write the code they review.

## Options to evaluate

### Option A: Microsoft Entra ID with managed identities

Use Microsoft Entra ID for all human authentication and Azure managed identities for service-to-service access. No stored credentials anywhere in the deployment chain.

Best fit when:
- All workloads run on Azure.
- The team can adopt Azure RBAC for resource access.
- GitHub Actions uses OIDC federation to Entra ID.

### Option B: Microsoft Entra ID with service principal secrets

Use service principal client secrets where managed identities are not available.

Best fit when:
- Third-party integrations require a credential that cannot use managed identity.

Risks:
- Secrets require rotation; stale secrets are a common breach vector.
- Requires Key Vault integration and rotation policy.

### Option C: External identity provider federation

Federate an existing organizational IdP into Microsoft Entra ID.

Best fit when:
- The organization already has an SSO provider (Okta, Ping, etc.) for clinical staff.

## Compliance notes

- `TODO(compliance): verify whether Texas PMP rules impose specific authentication requirements for prescribers accessing PMP data`
- `TODO(compliance): verify AWARxE/PMP InterConnect identity and credential requirements before implementing PDMP integration`
- `TODO(compliance): document HIPAA workforce access controls applicable to PHI-bearing Azure resources`

## Decision outcome

Pending. Complete before first shared-environment or production deployment.

## Review cadence

Review this record when:
- A new integration with a prescriber system or PDMP endpoint is added.
- Production deployment becomes planned.
- PHI data-handling scope changes.
- A new team role or service identity is required.
