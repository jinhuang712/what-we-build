# RUNBOOK.md

RUNBOOK.md is for the person keeping a service running. It is read under pressure, so each procedure is short and exact.

**Owns:**

- Deploy.
- Rollback.
- Monitoring.
- Each alert and its response.
- Who is on call.

## You have it when

- Someone paged at night can act from the page alone.
- Every alert has a response and a point to escalate.

## Skeleton

```markdown
# Runbook

## Deploy

<how to deploy, or the script that does>

## Roll back

<how to roll back, or the script that does>

## Alerts

<each alert, what to do, and when to escalate>

## On call

<who, and how to reach them>
```
