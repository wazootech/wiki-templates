---
id: wiki:ProcessOwnerShape
type: sh:NodeShape
rdfs:label: Process Owner Shape
rdfs:comment: Validation rules for process owner pages.
sh:targetClass: camunda:ProcessOwner
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owningTeam
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:responsibility
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Process Owner Shape

Validates process owner pages.
