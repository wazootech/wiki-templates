---
id: wiki:ServiceTaskShape
type: sh:NodeShape
rdfs:label: Service Task Shape
rdfs:comment: Validation rules for Camunda service task documentation.
sh:targetClass: camunda:ServiceTask
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:implementedBy
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:workerType
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Service Task Shape

Validates service task pages.
