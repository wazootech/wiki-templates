---
id: wiki:ConnectorShape
type: sh:NodeShape
rdfs:label: Connector Shape
rdfs:comment: Validation rules for connector documentation.
sh:targetClass: camunda:Connector
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:connectorId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owningSystem
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:owningTeam
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Connector Shape

Validates connector pages.
