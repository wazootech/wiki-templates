---
id: wiki:SLAShape
type: sh:NodeShape
rdfs:label: SLA Shape
rdfs:comment: Validation rules for service level agreement pages.
sh:targetClass: camunda:SLA
wazoo:jsonSchema: schemas/sla.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:targetDuration
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:escalationOwner
    sh:minCount: 1
    sh:datatype: xsd:string
---

# SLA Shape

Validates SLA pages.
