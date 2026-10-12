---
id: wiki:ComposedWorkspaceShape
type: sh:NodeShape
rdfs:label: Composed Workspace Shape
rdfs:comment: Validation rules for workspace overview pages in the umbrella corpus.
sh:targetClass: wspace:ComposedWorkspace
wazoo:jsonSchema: schemas/composed-workspace.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Composed Workspace Shape

Validates umbrella overview pages describing the composed workspace.
