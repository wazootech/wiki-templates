---
id: wiki:SubwikiSourceShape
type: sh:NodeShape
rdfs:label: Subwiki Source Shape
rdfs:comment: Validation rules for pages declaring a composed sub-wiki source.
sh:targetClass: wspace:SubwikiSource
wazoo:jsonSchema: schemas/subwiki-source.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: wspace:sourceRepo
    sh:minCount: 1
  - sh:path: wspace:sourceRef
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: wspace:sourcePath
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Subwiki Source Shape

Validates pages that declare a composed sub-wiki source.
