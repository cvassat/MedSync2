---
name: Dashboard metric task
description: Add, update, or retire a metric, KPI, or visualization in the MedSync2 dashboard layer.
title: "[Dashboard metric]: "
labels: ["dashboard-metric"]
assignees: []
---

## Objective

Describe the metric, KPI, chart, or dashboard panel this task should produce or change.

## Metric definition

- Metric name:
- Business question it answers:
- Numerator logic:
- Denominator logic (if rate):
- Aggregation level (patient, provider, clinic, population):
- Time grain (daily, weekly, monthly):

## Data sources

List the mart tables, views, or upstream sources this metric depends on.

- [ ]

## PHI and de-identification

- [ ] Metric is computed at an aggregate level that does not expose individual patient identity
- [ ] Underlying mart query uses surrogate keys or de-identified tokens, not raw patient identifiers
- [ ] No patient names, MRNs, DOBs, or SSNs appear in query results, exported data, or dashboard UI
- [ ] If a drill-through or row-level view is required, PHI access control is documented

If de-identification approach is not yet determined: `TODO(compliance): define de-identification strategy for <metric/query>`

## PDMP and PMP considerations

If this metric relates to PDMP access or PMP compliance:

- [ ] Score-only PDMP access and full-report PDMP review are tracked as separate fields
- [ ] Metric does not conflate `pdmp_score_accessed` with `pdmp_full_report_reviewed`
- [ ] Metric definition is reviewed by a compliance owner before implementation

## Source boundary

- [ ] Source-derived Azure point
- [ ] Current Microsoft documentation
- [ ] MedSync2-specific implementation decision
- [ ] General cloud-market analysis

## Acceptance criteria

- [ ] Metric definition documented and agreed with data owner
- [ ] No raw PHI in mart query or dashboard output
- [ ] PDMP score vs. full-report distinction maintained (if applicable)
- [ ] Dashboard tested against synthetic data
- [ ] `TODO(compliance):` and `TODO(vendor):` items filed or resolved

## Open assumptions

List anything not yet verified. Use `TODO(compliance):` or `TODO(source):` format.

- [ ]

## References

Add links to related issues, mart schema docs, decision records, or policy sources.
