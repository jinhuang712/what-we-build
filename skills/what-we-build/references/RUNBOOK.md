# RUNBOOK.md

RUNBOOK.md is for the person keeping a service running: how to deploy, roll back and respond to each alert. It is read under pressure, so each procedure is short and exact.

**Owns:** deploy, rollback, monitoring, each alert and its response, who is on call.

**Add when** the project is a service someone must keep running. Draft it after DESIGNS.md, once the service's parts are known.

| Weak | Strong |
|---|---|
| "Check the logs if something breaks." | "Alert `queue-lag > 5 min`: run `kubectl rollout restart deploy/worker`. If lag stays after 10 minutes, page the on-call." |
