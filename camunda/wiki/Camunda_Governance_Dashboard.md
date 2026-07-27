---
type: TechArticle
headline: Camunda Governance Dashboard
description: Rendered inventory of process, decision, task, and integration governance metadata.
---

# Camunda Governance Dashboard

## Processes and owners

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?process ?owner WHERE {
  ?doc rdf:type camunda:CamundaProcess .
  ?doc schema:headline ?process .
  ?doc camunda:owner ?owner .
}
ORDER BY ?process
```

| process | owner |
| --- | --- |
| Loan Approval Process | Underwriting Process Owner |

<!-- sparql:end -->

## Decisions and review cadence

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?decision ?cadence WHERE {
  ?doc rdf:type camunda:DmnDecision .
  ?doc schema:headline ?decision .
  ?doc camunda:reviewCadence ?cadence .
}
ORDER BY ?decision
```

| decision | cadence |
| --- | --- |
| Credit Risk Decision | P90D |

<!-- sparql:end -->

## BPMN models and process identifiers

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?model ?processId WHERE {
  ?doc rdf:type camunda:BpmnModel .
  ?doc schema:headline ?model .
  ?doc camunda:processId ?processId .
}
ORDER BY ?model
```

| model | processId |
| --- | --- |
| Loan Approval BPMN | loan-approval |

<!-- sparql:end -->

## Service tasks and implementation references

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?task ?impl WHERE {
  ?doc rdf:type camunda:ServiceTask .
  ?doc schema:headline ?task .
  OPTIONAL { ?doc camunda:implementedBy ?impl . }
}
ORDER BY ?task
```

| task | impl |
| --- | --- |
| Credit Bureau Service Task | Credit Bureau Job Worker |

<!-- sparql:end -->

## Tasks and forms

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?task ?form WHERE {
  ?task rdf:type camunda:UserTask .
  ?task schema:headline ?task .
  OPTIONAL { ?task camunda:usesForm ?form . }
}
ORDER BY ?task
```

(no results)

<!-- sparql:end -->

## SLAs and thresholds

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?sla ?target WHERE {
  ?doc rdf:type camunda:SLA .
  ?doc schema:headline ?sla .
  OPTIONAL { ?doc camunda:targetDuration ?target . }
}
ORDER BY ?sla
```

| sla | target |
| --- | --- |
| Loan Approval SLA | PT24H |

<!-- sparql:end -->

## Integrations and ownership

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?integration ?team WHERE {
  ?doc rdf:type camunda:SystemIntegration .
  ?doc schema:headline ?integration .
  ?doc camunda:owningTeam ?team .
}
ORDER BY ?integration
```

| integration | team |
| --- | --- |
| Core Banking System Integration | Integrations |

<!-- sparql:end -->

## KPI targets

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX camunda: <https://wazootech.github.io/wiki-camunda-template/ns/camunda#>

SELECT ?kpi ?target WHERE {
  ?doc rdf:type camunda:KPI .
  ?doc schema:headline ?kpi .
  ?doc camunda:targetValue ?target .
}
ORDER BY ?kpi
```

| kpi | target |
| --- | --- |
| First Pass Approval Rate KPI | 80% |

<!-- sparql:end -->
