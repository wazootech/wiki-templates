---
id: wiki:BpmnModelShape
type: sh:NodeShape
rdfs:label: BPMN Model Shape
rdfs:comment: Validation rules for BPMN model metadata pages.
sh:targetClass: camunda:BpmnModel
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:processId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:sourceFile
    sh:minCount: 1
    sh:datatype: xsd:string
---

# BPMN Model Shape

Validates BPMN model metadata pages.
