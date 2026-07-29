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

## Compliance sensitivity

Check every box that applies. If any box is checked, a **compliance reviewer must be added to the reviewers list** and must approve before merge.

- [ ] Touches PMP workflow logic or PDMP integration
- [ ] Encodes or modifies prescribing authority rules (PMHNP, MD, DO, PA, NP)
- [ ] References controlled-substance scheduling (Schedule II–V)
- [ ] Adds or changes patient-identifier handling, tokenization, or de-identification
- [ ] Modifies dashboard mart queries or reporting exports that could surface PHI
- [ ] Adds or changes a compliance flag, audit log field, or attestation record
- [ ] None of the above — compliance review not required for this PR

## PHI and data safety

- [ ] No real patient data (names, MRNs, DOBs, SSNs, diagnoses) is present in this PR
- [ ] All test fixtures use synthetic or clearly fake data
- [ ] Any new schema column that holds PHI is annotated with `# PHI: <description>`
- [ ] Raw patient identifiers are not passed through mart, dashboard, or reporting layers

## Policy logic

- [ ] No policy rules are invented or extrapolated without a verified citation
- [ ] All unverified policy assumptions are marked `TODO(compliance): <description>`
- [ ] All unknown vendor or source fields are marked `TODO(vendor):` or `TODO(source):`

## Risk review

- [ ] Security assumptions documented
- [ ] Cost assumptions documented
- [ ] Reliability assumptions documented
- [ ] Compliance assumptions documented
- [ ] Architecture decision record updated if needed

## Testing or validation

Describe the checks performed.

## Open follow-ups

List any remaining work or known limitations.
