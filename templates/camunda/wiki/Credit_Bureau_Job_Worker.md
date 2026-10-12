---
type: camunda:JobWorker
headline: Credit Bureau Job Worker
description: Worker that enriches applications with bureau data.
camunda:workerType: credit-bureau-check
camunda:implementedBy: java-client-example
camunda:usesConnector: Salesforce Connector
camunda:owner: Underwriting Process Owner
---

# Credit Bureau Job Worker

The worker polls for jobs, calls the bureau API, and returns normalized credit data to the process.

It implements [Credit Bureau Service Task](Credit_Bureau_Service_Task.md).
