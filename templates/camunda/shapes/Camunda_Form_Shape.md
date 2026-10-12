---
id: wiki:CamundaFormShape
type: sh:NodeShape
rdfs:label: Camunda Form Shape
rdfs:comment: Validation rules for Camunda form metadata pages.
sh:targetClass: camunda:CamundaForm
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:formId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:usedByTask
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Camunda Form Shape

Validates form metadata pages.
