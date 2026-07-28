---
name: Dashboard metric task
description: Add, modify, or validate a MedSync2 dashboard metric, KPI, or analytics view.
title: "[Dashboard Metric]: "
labels: ["dashboard-metric"]
assignees: []
---

## Objective

Describe the metric, KPI, or analytics view this task should produce and why it matters.

## Metric definition

| Property | Value |
|----------|-------|
| Metric name | |
| Business question answered | |
| Numerator | |
| Denominator | |
| Granularity (patient / prescriber / facility / population) | |
| Time window | |
| Data source(s) | |

## Scope

### In scope

- [ ]

### Out of scope

- [ ]

## Compliance checklist

- [ ] Metric does not expose raw patient identifiers in the output layer
- [ ] Aggregation or suppression rules applied for small cell sizes (specify threshold)
- [ ] PDMP-derived metrics correctly reflect full report review, not score-only retrieval, where required
- [ ] Prescribing authority metrics do not imply standalone Schedule II authority for outpatient PMHNPs
- [ ] PHI in underlying mart tables is de-identified or tokenized before metric calculation
- [ ] Data source for each input field is cited or marked `TODO(source-unknown):`

## Acceptance criteria

- [ ] Metric query uses no raw patient identifiers
- [ ] Source boundary documented for every input field
- [ ] Cell suppression or aggregation threshold defined for any patient-level output
- [ ] Dashboard view reviewed for unintended PHI exposure before deployment

## Evidence and references

Add links to metric specifications, clinical guidelines, source documents, or decision records.

## Open assumptions

- [ ]

## Notes
