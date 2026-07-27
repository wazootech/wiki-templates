---
type: sh:NodeShape
headline: Concept shape
description: SHACL constraints for concept and article pages in this LLM Wiki.
---

# Concept shape

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix wiki: <https://wazootech.github.io/llm-wiki-template/wiki/> .

wiki:ConceptShape
  a sh:NodeShape ;
  sh:targetClass schema:TechArticle ;
  sh:property [
    sh:path schema:headline ;
    sh:minCount 1 ;
    sh:datatype xsd:string ;
  ] ;
  sh:property [
    sh:path schema:description ;
    sh:minCount 1 ;
    sh:datatype xsd:string ;
  ] .
```

Use this shape for general knowledge articles compiled by agents from raw notes.
