# Security Policy

## Reporting a vulnerability

Do not disclose a suspected vulnerability in a public issue. Use GitHub's private security-advisory workflow for this repository and include:

- affected file or workflow;
- reproduction steps;
- expected and observed behavior;
- potential impact;
- any known mitigation.

## Current security boundary

The application is a calculation-only Streamlit interface. The repository does not currently implement authentication, authorization, a database, an API, audit logging, or a managed-secret integration.

This absence is not evidence that a public deployment is suitable for protected health information. A hosted Streamlit session transmits values between the user's browser and the application server even when the code does not intentionally persist them.

## Data-handling rules

- Do not enter patient names, dates of birth, medical-record numbers, addresses, or other identifiers.
- Do not log medication entries or calculation results.
- Do not commit secrets, credentials, tenant identifiers, subscription identifiers, or patient data.
- Treat screenshots, exported results, and server logs as potentially sensitive.

## Production deployment minimums

Before handling regulated or identifiable health information, document and approve at least:

- authentication and least-privilege authorization;
- HTTPS/TLS termination;
- network exposure and ingress controls;
- managed secret storage and rotation;
- logging, retention, and redaction rules;
- incident response and vulnerability-management ownership;
- backup and recovery requirements, if persistence is added;
- vendor agreements and compliance scope appropriate to the deployment.

No compliance certification or regulatory suitability is claimed by this repository.
