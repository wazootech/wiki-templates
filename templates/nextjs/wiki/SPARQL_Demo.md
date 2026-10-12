---
type: TechArticle
headline: SPARQL demo
description: Starter queries and wiring notes for the wiki-yasgui-template.
---

# SPARQL demo

Use this page as a typed `schema:TechArticle` target in filter queries.

## Sample SELECT

```sparql
PREFIX schema: <https://schema.org/>

SELECT ?person ?given ?family WHERE {
  ?person a schema:Person .
  ?person schema:givenName ?given .
  ?person schema:familyName ?family .
}
ORDER BY ?family
```

## Sample ASK

```sparql
PREFIX schema: <https://schema.org/>

ASK {
  ?doc a schema:TechArticle .
  ?doc schema:headline "SPARQL demo" .
}
```

## Related

- [Alice_Chen](Alice_Chen.md)
- [Bob_Martinez](Bob_Martinez.md)
