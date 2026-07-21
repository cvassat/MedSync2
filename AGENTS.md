# MedSync2 Coding-Agent Guidance

## Repository mission

MedSync2 is a calculation-only Streamlit application for estimating medication units required until a refill synchronization date. Preserve the distinction between mathematical planning and clinical, prescribing, dispensing, legal, or compliance decisions.

## Application invariants

1. Keep calculation logic in `medsync/calculator.py`; do not call Streamlit from the core module.
2. Use date-only semantics. Never calculate coverage from `datetime.now()` or a clock-dependent timedelta.
3. Compute unit shortfall directly:
   `max(coverage_days * daily_dose - units_remaining, 0)`.
4. Use `Decimal` for medication quantities and doses.
5. Treat both endpoint doses as explicit inputs. By default, cover only dates strictly between the calculation date and aligned refill date.
6. Do not log form entries, medication labels, or results.
7. Do not add autonomous clinical recommendations or represent output as medical advice.
8. Add regression tests for every calculation change.

## Required validation

Before completing a code change, run:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy medsync
python -m bandit -q -r medsync med_sync_app.py
python -m pytest
python -m compileall -q medsync med_sync_app.py tests
python -m pip_audit --requirement requirements.txt
```

## Sensitive-data guardrails

- Never place real patient data in code, tests, examples, screenshots, issues, or pull requests.
- Do not hard-code secrets, tenant IDs, subscription IDs, credentials, or environment-specific identifiers.
- Do not claim a deployment is HIPAA, HITRUST, SOC 2, FedRAMP, or otherwise compliant without verified scope, evidence, and approval.
- Any persistence, authentication, audit logging, external integration, or PHI handling requires an architecture/security review.

## Azure Essentials source boundary

When working from Azure Essentials material, keep these categories separate:

1. **Source-derived Azure points**: concepts traceable to the Azure Essentials resource kit or supplied update research.
2. **Current Microsoft documentation**: product names, navigation, pricing, compliance references, and implementation details that must be rechecked at time of use.
3. **MedSync2-specific decisions**: choices made after reviewing the actual code, product requirements, data flows, regulated-data posture, and deployment target.
4. **General cloud-market analysis**: neutral context that must not be represented as a Microsoft source claim.

Before adding cloud infrastructure, AI, compliance, or deployment code:

- update the applicable decision record in `docs/architecture/`;
- link work to `docs/cloud-adoption-backlog.md` or an issue;
- validate it against `docs/azure-essentials-operationalization.md`;
- document security, cost, reliability, data, and compliance assumptions;
- use hyphenated filenames for new user-facing documents, except required platform paths.

## Current Azure terminology baseline

Use current Microsoft terminology unless a legacy name is needed for searchability:

- Microsoft Foundry, formerly Azure AI Foundry.
- Microsoft Entra ID, formerly Azure Active Directory or Azure AD.
- Azure Proactive Resiliency Library v2 when referencing APRL guidance.
- Azure Well-Architected Framework when evaluating workload readiness.
- Azure Monitor Baseline Alerts when standardizing alerting baselines.
- Azure Verified Modules when evaluating reusable Bicep or Terraform modules.

Do not imply that the Azure Essentials source deck directly compares Azure and AWS.

## Recommended documents to keep current

- `README.md`: application orientation, calculation contract, and repository links.
- `docs/architecture/application-design.md`: application boundary and deterministic contract.
- `docs/azure-essentials-operationalization.md`: operating model and source boundary.
- `docs/cloud-adoption-backlog.md`: prioritized cloud execution queue.
- `docs/architecture/`: durable application and cloud architecture decisions.
- `docs/release-readiness-checklist.md`: release and deployment gate.
