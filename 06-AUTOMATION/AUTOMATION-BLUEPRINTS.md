# Automation Blueprints

## A. YouTube intelligence

Trigger: daily.

1. Read channel metrics.
2. Compare 1/7/30-day performance.
3. Identify rising topics.
4. Update opportunity database.
5. Produce CEO report.

## B. Content factory

Trigger: topic approved.

`brief → research → fact-check → script → title variants → thumbnail brief → production checklist → repurposing queue`

## C. Gold/data engine

`source → validation → normalized JSON → historical archive → website → social post`

Never publish stale or unverified prices as current.

## D. Tool SEO engine

`new tool → metadata → schema → internal links → sitemap → audit → report`

## E. NEPSE intelligence

`source → raw data → validation → normalized dataset → calculations → charts → explanation`

Keep raw facts separate from AI-generated interpretation.

## F. Social distribution

`approved content → platform adaptation → scheduling queue → publish → metrics → learning`

## G. Revenue dashboard

`platforms + websites + products → normalized metrics → monthly revenue report`

## Reliability requirements

Every automation needs:

- Trigger.
- Timeout.
- Retry policy.
- Validation.
- Logging.
- Failure notification.
- Idempotency where applicable.
- Manual override.
- Secret management through platform secrets/environment variables.

## GitHub Actions philosophy

Use Actions for deterministic scheduled work: data refreshes, audits, JSON generation, reports and deployment. Do not use a workflow as a substitute for a database when the workload requires transactional consistency.

## Data architecture

```text
raw/
  external-source.json

normalized/
  current.json

history/
  YYYY-MM-DD.json

reports/
  YYYY-MM-DD.md
```

## Human-in-the-loop

Require manual approval for:

- Sensitive news.
- Financial recommendations.
- Sponsored claims.
- Copyright-sensitive content.
- Irreversible production changes.
