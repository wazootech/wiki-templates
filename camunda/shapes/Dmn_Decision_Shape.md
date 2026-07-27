---
id: wiki:DmnDecisionShape
type: sh:NodeShape
rdfs:label: DMN Decision Shape
rdfs:comment: Validation rules for DMN decision pages.
sh:targetClass: camunda:DmnDecision
wazoo:jsonSchema: schemas/dmn-decision.json
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
  - sh:path: camunda:reviewCadence
    sh:minCount: 1
    sh:datatype: xsd:string
---

# DMN Decision Shape

Validates decision governance pages.
