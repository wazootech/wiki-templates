---
type: camunda:CamundaProcess
headline: Loan Approval Process
description: End-to-end process for intake, risk decisioning, manual review, and approval.
camunda:processId: loan-approval
camunda:bpmnModel: Loan_Approval_BPMN
camunda:owner: Underwriting Process Owner
camunda:hasDecision: Credit Risk Decision
camunda:hasUserTask: Manual Review User Task
camunda:hasServiceTask: Credit Bureau Service Task
camunda:hasSLA: Loan Approval SLA
camunda:usesIntegration: Salesforce Connector
camunda:reviewCadence: P90D
---

# Loan Approval Process

The process uses [Credit Risk Decision](Credit_Risk_Decision.md) to determine whether an application can be auto-approved or needs manual review.

Related pages:

- [Loan Approval BPMN](Loan_Approval_BPMN.md)
- [Underwriting Process Owner](Underwriting_Process_Owner.md)
- [Manual Review User Task](Manual_Review_User_Task.md)
- [Credit Bureau Job Worker](Credit_Bureau_Job_Worker.md)
