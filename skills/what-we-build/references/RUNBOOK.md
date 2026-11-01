# RUNBOOK.md

RUNBOOK.md is for the person keeping a service running.
It is read under pressure, so each procedure is short and exact.

**Owns:**

- Deploy.
- Rollback.
- Monitoring.
- Each alert and its response.
- Who is on call.

**Add when** the project is a service someone must keep running.
Draft it after DESIGNS.md, once the service's parts are known.

## You have it when

- Someone paged at night can act from the page alone.
- Every alert has a response and a point to escalate.

## Skeleton

```markdown
# Runbook

## Deploy
<commands>

## Roll back
<commands>

## Alerts

| Alert | Response | Escalate when |
|---|---|---|

## On call
<who, and how to reach them>
```
