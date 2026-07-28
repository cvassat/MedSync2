# Security Policy

## Supported versions

MedSync2 is currently pre-production. Security fixes are applied to the default branch only.

| Version | Supported |
|---|---|
| main (default) | ✅ |
| Other branches | ❌ |

## Reporting a vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report security vulnerabilities privately using [GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability) for this repository, or by contacting the repository owner directly through GitHub.

Include as much of the following information as possible:

- Type of vulnerability (for example, injection, authentication bypass, data exposure)
- Affected file(s) and line numbers
- Proof-of-concept or reproduction steps
- Potential impact, including whether PHI or patient data could be affected

## PHI and HIPAA considerations

MedSync2 operates in a regulated healthcare context. Any vulnerability that could expose Protected Health Information (PHI), enable unauthorized access to patient records, or bypass PDMP or PMP workflow controls is considered **critical severity** and will be triaged immediately.

## Response expectations

- Acknowledgement within 5 business days.
- Initial assessment within 10 business days.
- Coordinated disclosure timeline agreed with the reporter before any public disclosure.

## Scope

In-scope:

- Source code in this repository
- Deployment configuration and secrets handling
- Authentication and authorization logic
- PHI handling, de-identification, and tokenization logic
- PDMP and PMP workflow logic

Out of scope:

- Third-party services or Azure platform vulnerabilities (report directly to Microsoft)
- Vulnerabilities in dependencies that have a published CVE and an available fix (open a regular dependency update PR)

## Preferred languages

English.
