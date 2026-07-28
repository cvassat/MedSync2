---
name: Vendor mapping task
description: Track the mapping of a vendor-specific field, code set, or integration to MedSync2 internal schema.
title: "[Vendor mapping]: "
labels: ["vendor-mapping"]
assignees: []
---

## Objective

Describe the vendor system, integration endpoint, or field set to be mapped.

## Vendor and system details

- Vendor name:
- System or product:
- Integration type (HL7, FHIR, CSV, API, other):
- Known contact or documentation source:

## Fields to map

List each vendor field alongside the target MedSync2 field. Mark unknown fields with `TODO(vendor): confirm field name and semantics with <vendor>`.

| Vendor field | Vendor type | MedSync2 field | Notes / TODO |
|---|---|---|---|
| | | | |

## PHI considerations

- [ ] Vendor payload contains PHI (names, MRNs, DOBs, diagnoses, etc.)
- [ ] PHI is stripped or tokenized before storage
- [ ] Mapping does not surface raw identifiers in mart or reporting layers
- [ ] `# PHI: <description>` annotations added to relevant schema columns

## Policy dependencies

List any PMP, PDMP, DEA, or HIPAA rules that apply to this vendor's data. If a rule is unverified, add a `TODO(compliance):` entry.

- [ ]

## Source boundary

- [ ] Source-derived Azure point
- [ ] Current Microsoft documentation
- [ ] MedSync2-specific implementation decision
- [ ] Vendor documentation

## Acceptance criteria

- [ ] All vendor fields either mapped or marked `TODO(vendor):`
- [ ] PHI fields identified and de-identification approach documented
- [ ] Mapping table or transformation logic reviewed by a data owner
- [ ] Compliance-sensitive fields reviewed by a compliance owner if they encode policy rules
- [ ] Architecture decision record updated if the integration affects protected data flow

## Open assumptions

List anything not yet confirmed with the vendor. Use `TODO(vendor): confirm <field> with <vendor>` format.

- [ ]

## References

Add links to vendor documentation, HL7/FHIR specs, related issues, or decision records.
