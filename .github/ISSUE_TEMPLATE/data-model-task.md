---
name: Data model task
description: Propose or track a change to the MedSync2 data model, schema, or mart layer.
title: "[Data model]: "
labels: ["data-model"]
assignees: []
---

## Objective

Describe the data model change, new table or column, schema migration, or mart update this task should produce.

## Affected tables or entities

List the tables, views, marts, or domain objects involved.

- [ ]

## PHI and de-identification

- [ ] No raw patient identifiers (name, MRN, DOB, SSN) will be present in the target layer
- [ ] All PHI-bearing columns are annotated `# PHI: <description>` in the schema definition
- [ ] De-identification or tokenization mechanism is documented or linked below
- [ ] Surrogate keys or de-identified tokens are used in mart and reporting layers

If de-identification approach is not yet determined: `TODO(compliance): define de-identification strategy for <table/column>`

## Policy dependencies

List any PMP, PDMP, DEA, or HIPAA rules that constrain this schema change. If a rule is not yet verified, add a `TODO(compliance):` entry.

- [ ]

## Source boundary

- [ ] Source-derived Azure point
- [ ] Current Microsoft documentation
- [ ] MedSync2-specific implementation decision
- [ ] General cloud-market analysis

## Acceptance criteria

- [ ] Schema change is documented in `docs/architecture/` if it affects protected data flow
- [ ] No raw patient identifiers in mart or reporting layers
- [ ] All PHI columns annotated
- [ ] Migration script (if applicable) reviewed and tested against synthetic data
- [ ] `TODO(compliance):` and `TODO(vendor):` items are filed as follow-up issues or addressed

## Open assumptions

List anything not yet verified. Use `TODO(compliance):` or `TODO(vendor):` format.

- [ ]

## References

Add links to related issues, decision records, vendor docs, or policy sources.
