---
name: Compliance review task
description: Request a compliance review for a PR, feature, data model, or policy rule in MedSync2.
title: "[Compliance Review]: "
labels: ["compliance-review"]
assignees: []
---

## Objective

Describe the feature, PR, data model, or workflow rule that requires compliance review and the specific concern.

## Review type

- [ ] Clinical decision rule or prescribing authority logic
- [ ] PDMP query or workflow step
- [ ] De-identification or PHI handling
- [ ] Dashboard mart or analytics view
- [ ] Regulatory interpretation or policy encoding
- [ ] Other (describe below)

## Linked PR or issue

Add a link to the PR, issue, or commit that triggered this review.

## Compliance questions to resolve

List each specific question or uncertainty that the reviewer must answer before implementation proceeds. Use `TODO(compliance):` markers in code to cross-reference.

- [ ] TODO(compliance): 
- [ ] TODO(compliance): 

## Policy scope

Describe which policies, regulations, or vendor agreements are implicated (e.g., Texas PMP Act, DEA Schedule II rules, HIPAA Privacy Rule, vendor DUA).

## Hard-rule check

- [ ] Does this change encode standalone Schedule II prescribing authority for outpatient PMHNPs? _(Must be No)_
- [ ] Does this change treat score-only PDMP retrieval as full report review by default? _(Must be No)_
- [ ] Does this change expose raw patient identifiers in a dashboard mart or analytics export? _(Must be No)_

## Acceptance criteria

- [ ] All `TODO(compliance):` markers in the linked PR are resolved or deferred with documented rationale
- [ ] Reviewer has confirmed the policy source for each encoded clinical rule
- [ ] PHI exposure risk is assessed and mitigation documented
- [ ] Compliance reviewer has added a signoff comment on the linked PR

## Evidence and references

Add links to policy documents, vendor agreements, clinical guidelines, decision records, or prior compliance reviews.

## Reviewer notes

_(Compliance reviewer fills this section in.)_

## Open assumptions

- [ ]
