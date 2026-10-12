---
id: wiki:SystemIntegrationShape
type: sh:NodeShape
rdfs:label: System Integration Shape
rdfs:comment: Validation rules for system integration pages.
sh:targetClass: camunda:SystemIntegration
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owningSystem
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owningTeam
    sh:minCount: 1
    sh:datatype: xsd:string
---

# System Integration Shape

Validates integration pages.
