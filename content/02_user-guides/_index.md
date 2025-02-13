---
title: "User Guides"
date: 2025-02-11
weight: 3
---

{{% notice info %}}
- Milan requires time-aware switches. Use Switches that are Avnu certified. Other TSN Switches will likely not work out of the box.
- AVB Switches do not require QoS configuration like other Audio over IP protocols do.
- Make sure to set up the network in star topology
- Obey the rule of thumb for the maximum number of hops: 14hops for 1Gbps and 7 hops for 100Mbps.
- Use proper CAT cables
- Redundancy is achieved by physically separating the network. Obey different gPTP GMs for each network. Separate VLANs in the same switch will not work.
- The number of hops defines the latency in a Milan network. The smaller the number of hops, the smaller the network latency.
{{% /notice %}}

More details can be found in the following sections:

- Number of hops
- Switches
- Redundancy
- Quick Start Guide for Milan Manager

