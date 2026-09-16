---
name: cloud-hosting-cost-analysis
description: "Use when comparing VPS and scale-to-zero hosting costs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [cloud, hosting, vps, serverless, scale-to-zero, cost, migration]
---

# Cloud Hosting Cost Analysis

## When to Use

Use when a user asks whether a VPS, managed application host, free-tier VM, PaaS, or scale-to-zero platform would be cheaper or more appropriate for an existing workload. Also use for migration decisions where utilization is low but state, messaging, cron, or co-hosted services complicate the headline price comparison.

## Overview

Compare hosting options by actual workload economics and operational fit, not headline monthly price. This skill covers VPS, managed agent hosting, PaaS, free tiers, and scale-to-zero containers for stateful personal services and agents.

A strong answer identifies the cheapest *viable* option, computes the break-even utilization against the current host, checks memory/storage/network headroom, and accounts for every co-hosted service that would also need migration.

## Procedure

### 1. Establish the anchor

Verify the user's actual bill and current plan rather than assuming the provider's newest advertised plan. Record:

- monthly price including mandatory IP, storage, backup, and tax where known;
- vCPU, RAM, disk, transfer, location, SLA, and included backups;
- commitment term and renewal price;
- all services sharing the machine.

When live system access exists, measure current RAM/RSS, disk use, swap, CPU load, network usage, and long-running services. Treat page cache separately from process RSS and preserve operational headroom.

### 2. Define the workload's availability model

Classify it as:

- continuously active daemon;
- idle-but-listening gateway;
- webhook-triggered service;
- scheduled/cron workload;
- interactive batch workload.

For messaging agents, verify how an idle instance is awakened. A provider claiming scale-to-zero is insufficient unless inbound messages, scheduled jobs, and background completions can wake or remain reachable without an always-running poller.

### 3. Normalize monthly cost

For a scale-to-zero service, use:

```text
monthly cost = storage floor
             + active_fraction × (always-running cost - storage floor)
             + network/egress
             + mandatory platform fees
```

Compute the break-even active fraction against a fixed VPS:

```text
break_even = (VPS_monthly - storage_floor)
             / (always_running_cost - storage_floor)
```

Show at least the user's expected utilization and the break-even point. If the platform retains a warm instance after work, state that billed active time may exceed application busy time; do not equate “5% CPU busy” with “5% billable runtime” without the provider's idle policy.

### 4. Separate the latency layers

Do not conflate:

1. infrastructure wake/provisioning time;
2. container/process startup;
3. application initialization;
4. provider/model time-to-first-token.

A benchmark for application initialization does not prove scale-from-zero responsiveness. Prefer end-to-end idle-to-first-response p50/p95 measurements.

### 5. Test viability, not just price

Check:

- RAM headroom during startup, package installs, updates, and parallel jobs;
- persistent storage semantics and backup/restore;
- SQLite or file-lock behavior under horizontal concurrency;
- egress caps, public IPv4 charges, and inbound reachability;
- cron wake accuracy and missed-run handling;
- cold-start authentication/session restoration;
- architecture compatibility (x86_64 versus ARM64);
- preview/beta status and account/capacity risks.

Free tiers are valid candidates, but label quota, capacity, suspension, and support risks. Reject undersized tiers explicitly rather than presenting “$0” as a usable winner.

### 6. Account for migration scope

Inventory every co-hosted service before recommending cancellation. A managed single-app host may replace the primary workload but not sync daemons, backups, SSH workspaces, custom systemd units, or arbitrary shell access. Include the replacement cost and migration burden for those services.

### 7. Recommend by operating preference

Give three answers when they differ:

- **lowest monetary cost**;
- **lowest-operations option**;
- **best overall value/reliability**.

Quantify monthly and annual savings. Small savings rarely justify reduced backups, support, or reliability; say so plainly.

## Evidence and Verification

- Re-check official pricing immediately before answering; cloud prices and free-tier limits change frequently.
- Use official provider pages for load-bearing price/spec claims.
- Use live resource measurements when available.
- Perform all arithmetic with a tool.
- Label estimates and assumptions, especially billable idle/warm time.
- For a migration recommendation, advise a parallel trial covering cold wake, cron, persistence, and messaging delivery before cancelling the old host.

## Pitfalls

- Comparing a promotional annual rate against the user's month-to-month bill without labeling the commitment.
- Ignoring IPv4, volume, snapshot, backup, egress, or platform minimum charges.
- Treating application CPU utilization as serverless billable utilization.
- Using process startup benchmarks as evidence of infrastructure cold-start latency.
- Recommending a 512 MB–1 GB tier solely because steady-state RSS fits; startup and tool execution need headroom.
- Forgetting other services running on the existing VPS.
- Assuming a generic serverless container preserves local agent memory or SQLite safely.
- Recommending migration to save only a few dollars without pricing the user's time and reliability loss.

## References

- `references/hermes-agent-hosting.md` — Hermes-specific scale-to-zero economics, readiness checks, and a dated worked example.
