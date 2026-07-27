---
type: camunda:DmnDecision
headline: Credit Risk Decision
description: Decision model that scores applicant risk and routes borderline cases.
camunda:decisionId: credit-risk
camunda:owner: Underwriting Process Owner
camunda:reviewCadence: P90D
camunda:businessRationale: Balance approval speed against delinquency risk.
camunda:decisionTable: Applicant Eligibility Decision
---

# Credit Risk Decision

This decision references [Applicant Eligibility Decision](Applicant_Eligibility_Decision.md) and feeds the main process flow.
