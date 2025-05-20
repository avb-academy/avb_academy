---
title: "Traffic shaping"
date: 2025-02-11
weight: 4
---

{{% notice info %}}
- The bounded latency of Milan is ensured by using traffic shaping mechanisms.  
- The Stream Reservation Protocol (SRP) makes sure that the required bandwidth is available between a Talker and a Listener.  
- The Forward Queuing for Time-Sensitive Streams (FQTSS) ensures that packets are transmitted so that they reach their destination in time.  
- **Up to** 75% of the available bandwidth can be used for Milan traffic. If no stream requires the bandwidth, it is available for all other traffic.  
{{% /notice %}}

Traffic shaping is an essential part of Milan and the biggest difference compared to other networked audio protocols.

Two components are crucial for traffic shaping:

1. The [Stream Reservation Protocol](./stream-reservation/_index.md) (SRP) that configures a path from a Talker to a Listener.
2. The traffic shaper in a switch. The technology is based on the credit-based shaper and is often referred to as [Forwarding and Queuing for Time-Sensitive Streams](./fqtss/_index.md) (FQTSS).
