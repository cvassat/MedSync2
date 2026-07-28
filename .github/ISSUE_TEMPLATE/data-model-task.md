---
name: Data model task
description: Add, modify, or review a MedSync2 data model, table schema, or mart definition.
title: "[Data Model]: "
labels: ["data-model"]
assignees: []
---

## Objective

Describe the data model change, new table, or schema update this task should produce.

## Scope

### In scope

- [ ]

### Out of scope

- [ ]

## Compliance checklist

- [ ] No raw patient identifiers (MRN, name, DOB, SSN, contact info) in mart or analytics tables
- [ ] De-identification or tokenization strategy documented for any field that touches PHI
- [ ] Field-level source citation provided or `TODO(source-unknown): <field>` added for each column whose regulatory status is unclear
- [ ] Data retention and access-control assumptions documented

## Vendor and source mapping

List each external data source or vendor field this model depends on. If the field definition is unknown, add a `TODO(vendor-mapping): <vendor>/<field>` entry.

| Field | Source / Vendor | Mapping status |
|-------|----------------|---------------|
| | | ☐ Confirmed / ☐ TODO |

## Acceptance criteria

- [ ] Schema includes no raw patient identifiers in mart-facing views
- [ ] All PHI fields are clearly marked with de-identification method or `TODO(compliance):`
- [ ] Source boundary is documented for each new field
- [ ] Architecture decision record updated in `docs/architecture/` if this changes the data topology

## Evidence and references

Add links to source documents, vendor specs, ERDs, decision records, or Microsoft docs.

## Open assumptions

- [ ]

## Notes
