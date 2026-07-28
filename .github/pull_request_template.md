## Summary

Describe what changed and why it matters for MedSync2.

## Azure Essentials lifecycle stage

- [ ] Readiness and foundation
- [ ] Design and govern
- [ ] Manage and optimize
- [ ] Not applicable

## Source boundary

- [ ] Source-derived Azure point
- [ ] Current Microsoft documentation
- [ ] MedSync2-specific implementation decision
- [ ] General cloud-market analysis
- [ ] Not applicable

## Compliance checklist

_Complete every item that applies. PRs touching clinical rules, PDMP logic, prescribing authority, or de-identification cannot merge without these._

- [ ] No PHI or real patient identifiers committed (source code, tests, fixtures, docs, comments)
- [ ] No regulatory or clinical rules encoded without an explicit source citation or `TODO(compliance):` marker
- [ ] All unknown vendor fields or PDMP data elements marked with `TODO(vendor-mapping):` or `TODO(source-unknown):`
- [ ] Dashboard mart queries and analytics views use de-identified or tokenized references only
- [ ] Prescribing authority logic does not grant standalone Schedule II authority to outpatient PMHNPs
- [ ] PDMP workflow correctly distinguishes score-only retrieval from full report review
- [ ] `compliance-review` label added and designated reviewer tagged if this PR modifies clinical decision rules, PDMP queries, prescribing authority checks, or de-identification logic

## Risk review

- [ ] Security assumptions documented
- [ ] Cost assumptions documented
- [ ] Reliability assumptions documented
- [ ] Compliance assumptions documented
- [ ] Architecture decision record updated if needed (`docs/architecture/`)

## Testing or validation

Describe the checks performed.

## Open follow-ups

List any remaining work, known limitations, or unresolved `TODO(compliance):` items.
