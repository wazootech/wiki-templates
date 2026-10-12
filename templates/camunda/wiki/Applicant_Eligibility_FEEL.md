---
type: camunda:FeelExpression
headline: Applicant Eligibility FEEL
description: FEEL expression used by the applicant eligibility decision table.
camunda:expressionId: applicant-eligibility-feel
camunda:owner: Underwriting Process Owner
camunda:expressionLanguage: FEEL
camunda:businessRationale: Concentrate field checks in a readable, testable expression.
---

# Applicant Eligibility FEEL

Example expression:

```feel
applicant.score >= 650 and applicant.income >= 40000
```
