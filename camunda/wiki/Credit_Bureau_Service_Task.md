---
type: camunda:ServiceTask
headline: Credit Bureau Service Task
description: Service task that invokes bureau enrichment during loan screening.
camunda:taskId: credit-bureau-check
camunda:implementedBy: Credit Bureau Job Worker
camunda:usesConnector: Salesforce Connector
camunda:workerType: credit-bureau-check
camunda:owner: Underwriting Process Owner
---

# Credit Bureau Service Task

This service task is the BPMN-facing contract. The worker page records the implementation behind it.
