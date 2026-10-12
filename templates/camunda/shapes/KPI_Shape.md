---
id: wiki:KPIShape
type: sh:NodeShape
rdfs:label: KPI Shape
rdfs:comment: Validation rules for KPI pages.
sh:targetClass: camunda:KPI
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:metricName
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:targetValue
    sh:minCount: 1
    sh:datatype: xsd:string
---

# KPI Shape

Validates KPI pages.
