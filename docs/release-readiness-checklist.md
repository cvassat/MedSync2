# MedSync2 Release Readiness Checklist

Use this gate before merging or deploying a release.

## Application behavior

- [ ] Date inclusion/exclusion semantics are unchanged or explicitly reviewed.
- [ ] Direct unit arithmetic remains `max(coverage days × daily dose - units remaining, 0)`.
- [ ] Fractional quantities remain exact in the calculation layer.
- [ ] Same-day, past-date, excess-on-hand, and non-divisible-quantity cases pass.
- [ ] User-facing text does not imply prescribing, dispensing, legal, or clinical advice.

## Automated assurance

- [ ] `python -m ruff check .`
- [ ] `python -m ruff format --check .`
- [ ] `python -m mypy medsync`
- [ ] `python -m bandit -q -r medsync med_sync_app.py`
- [ ] `python -m pytest`
- [ ] `python -m compileall -q medsync med_sync_app.py tests`
- [ ] `python -m pip_audit --requirement requirements.txt`
- [ ] CodeQL completes without unresolved high-severity findings.
- [ ] Dependency review passes for introduced or changed dependencies.
- [ ] Dependabot alerts and version-update pull requests are triaged.

## Privacy and security

- [ ] No patient data, credentials, secrets, or environment identifiers appear in the diff.
- [ ] Form values and results are not logged.
- [ ] Browser error details remain suppressed outside controlled development environments.
- [ ] CORS and XSRF protections remain enabled.
- [ ] TLS is terminated by an approved ingress, proxy, or managed platform.
- [ ] Authentication and authorization are approved before any identifiable-data use.
- [ ] Retention, logging, incident-response, and evidence ownership are documented for production.

## Deployment

- [ ] Container runs as a non-root user.
- [ ] Health check passes.
- [ ] Runtime dependency audit passes against the final image or environment.
- [ ] Environment promotion and rollback are documented.
- [ ] Cookie secret and other deployment secrets are injected through approved secret management.
- [ ] The Azure landing-zone and data-protection decision records are completed before production.

## Governance

- [ ] Reviewers confirm the repository has an approved license before external reuse or distribution.
- [ ] Branch protection and required status checks are enabled for `main`.
- [ ] Secret scanning and dependency graph features are enabled.
- [ ] Residual risks are accepted by an identified owner.
