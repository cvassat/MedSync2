# MedSync2

MedSync2 is a Streamlit-based planning calculator that estimates additional medication units needed between a calculation date and an aligned refill date.

> **Important:** This is a mathematical planning aid, not medical advice or a prescribing/dispensing system. Independently verify every result. Do not enter patient identifiers unless a deployment has been specifically approved for that data.

## Hardened baseline

- Date-only calculations eliminate clock-time off-by-one behavior.
- Direct unit arithmetic eliminates floor-division overestimation.
- Fractional doses and remaining quantities use `Decimal` precision.
- Calculation logic is separated from the Streamlit presentation layer.
- Endpoint inclusion is explicit for both the calculation date and aligned refill date.
- Validation, regression tests, app tests, linting, typing, security scanning, dependency auditing, CodeQL, dependency review, Dependabot, and container hardening are included.
- Privacy, clinical, deployment, and compliance limitations are explicit.

## Calculation model

Coverage days are the calendar dates whose doses must be supplied by the entered on-hand or bridge quantity.

- The calculation-date dose is excluded by default and included only when it remains outstanding.
- The aligned-refill-date dose is excluded by default and included only when the bridge quantity must cover it.
- When the dates differ, dates strictly between them are always counted.
- When both dates are the same, that calendar date is counted once when either endpoint option is selected.

For each medication:

```text
target units = coverage days * daily dose
additional units = max(target units - units remaining, 0)
```

## Run locally

Requires Python 3.12 or 3.13.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements.txt
streamlit run med_sync_app.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Development checks

```bash
python -m pip install --requirement requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m mypy medsync
python -m bandit -q -r medsync med_sync_app.py
python -m pytest
python -m compileall -q medsync med_sync_app.py tests
python -m pip_audit --requirement requirements.txt
```

## Container

```bash
docker build -t medsync2 .
docker run --rm -p 8501:8501 medsync2
```

Then open `http://localhost:8501`.

## Repository layout

- `med_sync_app.py`: Streamlit presentation layer.
- `medsync/calculator.py`: pure validation and calculation logic.
- `tests/`: regression and Streamlit application tests.
- `docs/architecture/application-design.md`: application contract, boundaries, and exclusions.
- `docs/code-review-and-hardening-report-2026-07-21.md`: review findings, remediation, and residual risks.
- `docs/release-readiness-checklist.md`: pre-merge and pre-deployment gate.
- `SECURITY.md`: security reporting and production-control requirements.
- `docs/azure-essentials-operationalization.md`: existing cloud-adoption governance and source boundary.
- `docs/cloud-adoption-backlog.md`: existing cloud implementation backlog.
- `docs/architecture/azure-landing-zone-decision-record.md`: existing pre-production Azure decision scaffold.

## Privacy and compliance boundary

The repository does not currently implement authentication, authorization, persistent storage, audit logging, or a regulated production environment. The application code does not intentionally persist entries, but hosted use transmits values between browser and server. See `SECURITY.md` before any deployment involving sensitive or regulated data.

No claim of HIPAA, HITRUST, SOC 2, FedRAMP, or other compliance status is made.

## Known limitations

This calculator does not account for variable dosing, PRN use, tapers, adherence, package sizes, insurance restrictions, controlled-substance rules, pharmacy policies, or clinical appropriateness. It does not choose dispensing increments or round quantities for a pharmacy.

## Azure Essentials operating model

The repository's existing cloud-adoption package organizes future cloud work into three stages:

1. **Readiness and foundation:** identity, environments, landing zone, cost baseline, repository controls, and data assumptions.
2. **Design and govern:** architecture, policy, review gates, AI guardrails, and deployment decisions.
3. **Manage and optimize:** observability, reliability, backup and restore, cost review, and ongoing remediation.

Azure guidance informs planning; final implementation decisions still require current Microsoft documentation, actual product requirements, and approved data/compliance assumptions.
