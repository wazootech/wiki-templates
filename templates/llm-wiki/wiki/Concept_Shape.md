---
id: wiki:ConceptShape
type: sh:NodeShape
headline: Concept shape
description: SHACL constraints for concept and article pages in this LLM Wiki.
sh:targetClass: schema:TechArticle
sh:property:
  - sh:path: schema:headline
    sh:datatype: xsd:string
    sh:minCount: 1
  - sh:path: schema:description
    sh:datatype: xsd:string
    sh:minCount: 1
---

# Concept shape

Use this shape for general knowledge articles compiled by agents from raw notes.
