---
id: wiki:UserTaskShape
type: sh:NodeShape
rdfs:label: User Task Shape
rdfs:comment: Validation rules for Camunda user task pages.
sh:targetClass: camunda:UserTask
wazoo:jsonSchema: schemas/user-task.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:taskId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:assignedRole
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:usesForm
    sh:minCount: 1
    sh:datatype: xsd:string
---

# User Task Shape

Validates user task pages.
