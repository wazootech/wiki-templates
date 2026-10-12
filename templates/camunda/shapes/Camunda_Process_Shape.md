---
id: wiki:CamundaProcessShape
type: sh:NodeShape
rdfs:label: Camunda Process Shape
rdfs:comment: Validation rules for Camunda process governance pages.
sh:targetClass: camunda:CamundaProcess
wazoo:jsonSchema: schemas/camunda-process.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:processId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owner
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:hasSLA
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Camunda Process Shape

Validates process governance pages.
