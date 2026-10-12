---
id: wiki:JobWorkerShape
type: sh:NodeShape
rdfs:label: Job Worker Shape
rdfs:comment: Validation rules for job worker documentation.
sh:targetClass: camunda:JobWorker
wazoo:jsonSchema: schemas/job-worker.json
sh:property:
  - sh:path: schema:headline
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:workerType
    sh:minCount: 1
    sh:datatype: xsd:string
  - sh:path: camunda:implementedBy
    sh:minCount: 1
    sh:datatype: xsd:string
---

# Job Worker Shape

Validates job worker pages.
