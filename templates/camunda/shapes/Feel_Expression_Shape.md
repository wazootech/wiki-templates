---
id: wiki:FeelExpressionShape
type: sh:NodeShape
rdfs:label: FEEL Expression Shape
rdfs:comment: Validation rules for FEEL expression documentation pages.
sh:targetClass: camunda:FeelExpression
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:expressionId
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:expressionLanguage
    sh:minCount: 1
    sh:datatype: xsd:string
---

# FEEL Expression Shape

Validates FEEL expression pages.
