# Hermes Agent Hosting: Scale-to-Zero Evaluation

Use this reference when comparing a conventional VPS with Nous Hermes Cloud, generic serverless containers, or free-tier VMs. Re-verify all prices and product status before answering.

## Workload-specific checks

Hermes is stateful and commonly combines:

- a messaging gateway that must receive or poll for messages;
- cron jobs that must wake reliably;
- SQLite session state, memory, skills, credentials, and workspace files;
- background tasks and subagents that may outlive the initiating request;
- arbitrary terminal work with bursty memory and disk needs.

A credible scale-to-zero host must preserve `$HERMES_HOME`, wake from configured messaging channels and cron, and avoid concurrent writers corrupting or locking state. Test finished-response delivery across a sleep/restart boundary.

## Latency terminology

Measure these independently:

1. idle platform → container scheduled;
2. container → Hermes process ready;
3. Hermes ready → model request dispatched;
4. model request → first token;
5. first token → delivered message.

Hermes initialization improvements do not establish managed-cloud wake latency. Ask for or measure idle-to-Telegram-response p50/p95.

## Dated worked example — 2026-08-10

Recheck before reuse.

- OVH VPS-1 public offer: `$4.54/month`, 2 vCPU, 4 GB RAM, 40 GB NVMe, daily backup, unlimited traffic.
- Nous Hermes Cloud Small: 2 vCPU, 1 GB RAM, `$0.29/day` running and `$0.03/day` stopped; inference and tool use excluded.
- For a 30-day month:
  - storage floor = `30 × 0.03 = $0.90`;
  - always running = `30 × 0.29 = $8.70`;
  - at 5% billable active time = `$0.90 + 0.05 × ($8.70 - $0.90) = $1.29`;
  - break-even against `$4.54` = `(4.54 - 0.90) / (8.70 - 0.90) = 46.7%`, about 11.2 billable hours/day.

The 5% estimate is valid only if application activity approximately matches provider-billed runtime. Warm retention, startup, background tasks, or daily billing granularity can raise the effective fraction.

## Capacity interpretation

A steady-state gateway RSS around 300 MB does not make a generic 512 MB tier safe. Python/Node startup, package operations, tools, compression, and delegated tasks need burst headroom. A managed 1 GB Hermes tier may be tuned for the workload; an arbitrary 1 GB VM with OS overhead and co-hosted daemons is a different proposition.

## Migration-scope trap

Before recommending cancellation, inspect the old VPS for unrelated services such as Obsidian sync, monitoring, backups, websites, VPNs, or custom systemd units. Hermes Cloud is an application host, not automatically a replacement for a general-purpose SSH box. Price the destination for every remaining service.

## Practical recommendation pattern

- Lowest-ops low-utilization Hermes-only workload: trial managed Hermes Cloud in parallel.
- Lowest monetary cost with more operational risk: evaluate a current always-free VM with enough RAM/storage and verify capacity/account policy.
- Mixed Hermes plus other persistent services: a low-cost VPS may remain the best overall value even when the agent itself is mostly idle.

Do not cancel the old host until Telegram wake, cron execution, state persistence, backups, and long-running task delivery have passed a parallel trial.
