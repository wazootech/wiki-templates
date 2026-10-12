---
id: wiki:DecisionTableShape
type: sh:NodeShape
rdfs:label: Decision Table Shape
rdfs:comment: Validation rules for decision table pages.
sh:targetClass: camunda:DecisionTable
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:decisionId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owner
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Decision Table Shape

Validates decision table pages.
