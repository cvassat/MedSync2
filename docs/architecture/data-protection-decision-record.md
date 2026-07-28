# Data Protection Decision Record

Status: draft

Date: 2026-07-28

## Decision

MedSync2 has not yet finalized its data protection, PHI handling, or compliance evidence posture. This record defines the minimum decisions required before any production deployment that touches protected health information or regulated prescribing workflows.

## Context

MedSync2 is a medication synchronization tool that may process or display data covered by HIPAA, the Texas Health & Safety Code (Chapter 481 and PDMP provisions), and DEA scheduling rules. This record documents data classification, encryption, retention, access control, de-identification, and audit requirements before any production data flows are enabled.

## Data classification

| Data class | Examples | PHI? | Regulatory reference | Status |
|---|---|---|---|---|
| Patient medication records | Name, MRN, medication name, dose, refill date | Yes | HIPAA, Texas HSC | `TODO(compliance): confirm full field list with clinical lead` |
| Prescriber identity | NPI, DEA number, name, practice address | Sensitive | Texas PMP, DEA | `TODO(compliance): confirm prescriber data handling requirements` |
| PDMP query and response | Controlled-substance history, dispenser records | Yes | Texas PDMP, HIPAA | `TODO(compliance): verify PDMP data retention requirements` |
| Audit logs | User, action, resource, timestamp | Sensitive (may contain PHI references) | HIPAA audit controls | `TODO(compliance): confirm minimum audit log retention period` |
| Synthetic/test data | Fake patient IDs, fake MRNs | No | N/A | Must be clearly labeled; no real data in repo |
| Application configuration | Environment variables, feature flags | No (unless contains identifiers) | N/A | No PHI allowed |

## Required decisions

| Area | Current answer | Owner | Status |
|---|---|---|---|
| PHI data stores | Not yet selected | To be assigned | Open |
| Encryption at rest | Azure-managed keys minimum; customer-managed keys required if HIPAA BAA mandates it | To be assigned | Open |
| Encryption in transit | TLS 1.2 minimum for all network communication | To be assigned | Draft assumption |
| Backup and retention | Automated backup required for PHI stores; retention period to be determined by compliance | To be assigned | Open |
| Data residency | US-only Azure regions required for PHI | To be assigned | Draft assumption |
| De-identification approach | Surrogate keys or tokenization at mart/reporting boundary | To be assigned | Open |
| PDMP data retention | `TODO(compliance): verify Texas PDMP data retention rules` | To be assigned | Open |
| Business Associate Agreement | Required with any vendor that processes PHI on MedSync2's behalf | To be assigned | Open |
| PHI in logs | PHI must not appear in application logs, error messages, or metrics | To be assigned | Draft assumption |
| Breach notification procedure | To be determined; must meet HIPAA 60-day notification requirement | To be assigned | Open |
| Compliance evidence location | `docs/architecture/` for policy records; separate secure store for evidence artifacts | To be assigned | Open |

## Design constraints

1. **No raw patient identifiers in marts, dashboards, or reporting layers.** All analytics and reporting layers must use surrogate keys or de-identified tokens. Direct patient identifiers (name, MRN, DOB, SSN, address) must not appear in any query result, export, or UI component outside the clinical access boundary.
2. **Separate PDMP score-access and full-report review.** Accessing a risk score or summary does not satisfy the Texas PDMP full-report review requirement. These must be tracked as distinct fields: `pdmp_score_accessed` and `pdmp_full_report_reviewed`. Do not conflate them.
3. **No PHI in the repository.** Source code, tests, fixtures, configuration, and documentation must never contain real patient data. Use synthetic data with clearly fake identifiers (`patient_id: "TEST-001"`, `mrn: "FAKE-MRN-12345"`).
4. **PHI column annotation.** Any schema column, model field, or function parameter that holds PHI must be annotated with `# PHI: <description>` and the de-identification or access-control mechanism documented here.
5. **Audit log integrity.** Audit logs must be write-once or append-only and stored separately from application data. Tampering detection (hashing, Azure Monitor integration) is required before production.

## Known PHI-bearing fields (incomplete — update as schema is defined)

```
# PHI: patient legal name
patient_name

# PHI: pharmacy-assigned medical record number
mrn

# PHI: date of birth
date_of_birth

# PHI: controlled-substance prescription records (PDMP data)
pdmp_query_response

# PHI: medication name and dose (may imply diagnosis)
medication_name
daily_dose
```

## Compliance notes

- `TODO(compliance): obtain and document HIPAA Business Associate Agreement with Azure (Microsoft)`
- `TODO(compliance): verify Texas PDMP data-handling requirements under Texas Health & Safety Code §481.076`
- `TODO(compliance): verify DEA requirements for storage and retention of Schedule II–V prescription records`
- `TODO(compliance): document breach notification procedure meeting HIPAA 45 CFR §164.404`
- `TODO(compliance): determine whether MedSync2 deployment qualifies as a covered entity, business associate, or both`

## Decision outcome

Pending. Complete before any PHI is processed in a shared or production environment.

## Review cadence

Review this record when:
- A new PHI-bearing data store or integration is added.
- PDMP or PMP integration scope changes.
- Encryption, retention, or de-identification approach is finalized.
- A compliance audit, BAA negotiation, or breach notification is triggered.
