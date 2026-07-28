---
name: Vendor mapping task
description: Map a vendor API, PDMP data feed, pharmacy system, or external integration to MedSync2 fields.
title: "[Vendor Mapping]: "
labels: ["vendor-mapping"]
assignees: []
---

## Objective

Describe the vendor integration or field mapping this task should produce.

## Vendor / integration

Name of the vendor, API, or data feed (e.g., Bamboo Health PDMP, Surescripts, Epic FHIR).

## Scope

### In scope

- [ ]

### Out of scope

- [ ]

## Field mapping table

Document each vendor field and its MedSync2 target. Mark any field whose mapping is unconfirmed with `TODO(vendor-mapping):`.

| Vendor field | MedSync2 field | Data type | PHI? | Mapping status |
|-------------|---------------|----------|------|---------------|
| | | | ☐ Yes / ☐ No | ☐ Confirmed / ☐ TODO |

## Compliance checklist

- [ ] Vendor contract or data-use agreement confirmed before implementation begins
- [ ] PHI fields identified and de-identification strategy documented
- [ ] No raw patient identifiers passed to dashboard marts or analytics exports
- [ ] PDMP fields clearly distinguish score-only data from full report data
- [ ] All unconfirmed mappings marked `TODO(vendor-mapping): <vendor>/<field>`

## Acceptance criteria

- [ ] All confirmed field mappings are documented with source citations
- [ ] Unconfirmed mappings have `TODO(vendor-mapping):` markers in code and in this issue
- [ ] PHI handling strategy is reviewed before any mapping is implemented in production code
- [ ] Architecture decision record updated in `docs/architecture/` if this changes integration topology

## Evidence and references

Add links to vendor API docs, data dictionaries, DUAs, decision records, or related issues.

## Open assumptions

- [ ]

## Notes
