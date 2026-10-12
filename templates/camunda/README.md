# wiki-camunda-template

Starter repository for a Camunda process and rules knowledge base powered by **Wiki CLI**.

Camunda owns BPMN/DMN execution, job workers, connectors, forms, Optimize, and runtime state. Wiki CLI owns the semantic layer around it: process docs, governance metadata, SHACL/JSON Schema validation, SPARQL dashboards, and static publishing.

Use this template when you want a documented Camunda project with machine-readable governance, not a runtime replacement.

## Quick start

1. Click **Use this template** on GitHub, or clone the repo.
2. Install [Wiki CLI](https://pypi.org/project/wazootech-wiki/):

```bash
pip install wazootech-wiki
```

3. Validate and preview:

```bash
wiki -c wiki.yml fmt --check
wiki -c wiki.yml lint --strict
wiki -c wiki.yml check --strict
wiki -c wiki.yml render --check
wiki -c wiki.yml serve --watch
```

4. Enable **Settings → Pages → Source: GitHub Actions** so the deploy workflow can publish the built site.

## Workspace layout

- `wiki.yml` - config root (`wiki.input`, `graph.*`, `site.*`)
- `wiki/` - Camunda process, decision, worker, and governance pages
- `shapes/` - SHACL shapes and optional JSON Schema bindings
- `layouts/` - Jinja page templates
- `assets/` - static files copied on `wiki build`
- `schemas/` - JSON Schema files used by selected shapes

## Starter corpus

- `Loan_Approval_Process.md` - end-to-end process governance page
- `Credit_Risk_Decision.md` - decision metadata and review cadence
- `Applicant_Eligibility_Decision.md` - decision table / FEEL rule docs
- `Manual_Review_User_Task.md` - human task and form ownership
- `Salesforce_Connector.md` - integration contract
- `Credit_Bureau_Job_Worker.md` - worker implementation reference
- `Underwriting_Process_Owner.md` - stakeholder and ownership record
- `Process_SLA_Catalog.md` - SLA/KPI inventory
- `Camunda_Governance_Dashboard.md` - rendered SPARQL governance tables
- `Camunda_Standards.md` - Camunda and OMG source references

## Checks

| Command | Purpose |
| ------- | ------- |
| `wiki fmt` | Mechanical markdown layout |
| `wiki lint --strict` | Broken links, filename pattern, heading conventions |
| `wiki check --strict` | SHACL, JSON Schema, routes, layout integrity |
| `wiki render --check` | Stale inline SPARQL blocks |
| `wiki build` | Static HTML for deployment |

## Deployment

The repo builds to a static site at `/wiki-camunda-template/` on GitHub Pages.

### GitHub Pages

1. Go to **Settings → Pages → Source: GitHub Actions**.
2. Push to `main`.
3. The workflow publishes the built site automatically.

### Other static hosts

Any host that serves static files works. Use `wiki build --output-dir _site --site-base-url /wiki-camunda-template`.

## Related

- [Wiki CLI](https://github.com/wazootech/wiki)
- [Camunda Java Client](https://docs.camunda.io/docs/apis-tools/java-client/getting-started/)
- [BPMN 2.0](https://www.omg.org/spec/BPMN/2.0/)
- [DMN](https://www.omg.org/dmn/)
