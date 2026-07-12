# Azure Landing Zone Decision Record

Status: draft

Date: 2026-07-03

## Decision

MedSync2 has not yet selected a final Azure landing-zone topology. This record defines the minimum decision fields that must be completed before production cloud deployment.

## Context

The Azure Essentials operating model treats landing zones, financial controls, identity, governance, security, and operational readiness as prerequisites for scaled cloud adoption. For MedSync2, that means deployment decisions should not be made solely at the application-runtime level.

## Required decisions

| Area | Current answer | Owner | Status |
|---|---|---|---|
| Azure tenant | To be determined | To be assigned | Open |
| Subscription strategy | To be determined | To be assigned | Open |
| Environments | Development, test/staging, and production are expected but not approved | To be assigned | Open |
| Primary Azure region | To be determined | To be assigned | Open |
| Secondary or disaster-recovery region | To be determined | To be assigned | Open |
| Management groups | To be determined | To be assigned | Open |
| Network topology | To be determined | To be assigned | Open |
| Identity provider | Microsoft Entra ID assumed for Azure-native identity decisions | To be assigned | Draft assumption |
| Secret-management approach | Managed secret store required; implementation to be selected | To be assigned | Open |
| Logging and monitoring | Azure Monitor-aligned baseline expected | To be assigned | Open |
| Compliance evidence location | To be determined | To be assigned | Open |
| Cost owner | To be determined | To be assigned | Open |

## Options to evaluate

### Option A: Simple application landing zone

Use a minimal Azure subscription/environment structure for early development while retaining clear separation of development and production.

Best fit when:

- MedSync2 is still pre-production or early-stage.
- Deployment volume is low.
- The team needs fast delivery with explicit guardrails.

Risks:

- Controls may need rework as the system scales.
- Shared services might be under-designed.

### Option B: Platform plus application landing zones

Use a platform landing zone for shared identity, connectivity, management, monitoring, and policy controls, plus one or more application landing zones for MedSync2 workloads.

Best fit when:

- MedSync2 will process regulated or sensitive data.
- Multiple environments or workloads are expected.
- Centralized governance, monitoring, and policy enforcement are required.

Risks:

- Requires more initial architecture and platform effort.
- Can slow early development if overbuilt.

### Option C: Defer Azure deployment decision

Keep the repository cloud-ready but avoid selecting an Azure topology until application architecture, data classification, and deployment requirements are clearer.

Best fit when:

- The codebase does not yet contain enough implementation detail to justify cloud topology decisions.
- Product and compliance requirements are unresolved.

Risks:

- Infrastructure decisions may become rushed later.
- Cost and reliability planning remain abstract.

## Recommended next step

Complete the P0 backlog items before selecting the final deployment topology:

1. Identity and access decision record.
2. Data-protection decision record.
3. Cost-management plan.
4. Observability decision record.

## Decision outcome

Pending.

## Review cadence

Review this record whenever one of the following changes:

- New environment is added.
- Production deployment becomes planned.
- PHI, PII, or regulated workflow assumptions change.
- AI or agent functionality is introduced.
- External integration scope changes.
