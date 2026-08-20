---
id: wiki:WorkspaceDecisionShape
type: sh:NodeShape
rdfs:label: Workspace Decision Shape
rdfs:comment: Validation rules for architecture decision records in the workspace corpus.
sh:targetClass: wspace:WorkspaceDecision
wazoo:jsonSchema: schemas/workspace-decision.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: wspace:status
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: wspace:decisionOwner
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: wspace:decisionDate
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Workspace Decision Shape

Validates architecture decision record pages.
