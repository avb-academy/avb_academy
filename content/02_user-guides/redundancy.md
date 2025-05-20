---
title: "Redundancy"
date: 2025-02-11
weight: 50
---

Redundancy is an optional feature in Milan. Therefore, not all Milan devices support redundancy.

For a Milan network to be redundant, it must use physically separate networks. This means that the {{< tooltip "Primary">}} and {{< tooltip "Secondary">}} network each require their own dedicated {{< tooltip "Switch" "Switches">}}. Physical separation is necessary due to the way Milan operates. Specifically, each network must have its own {{< tooltip "gPTP">}} GrandMaster to maintain proper synchronization. The election of a {{< tooltip "gPTP">}} GrandMaster is described in [Network Timing :: Clock Leader Election](../01_milan/00_network-timing/#clock-leader-election).

Redundancy ensures that a pair of redundant ports ({{< tooltip "Primary">}} and {{< tooltip "Secondary">}}) continuously transmit the same audio data. As a result, both networks require identical bandwidth. In the event of a failure, seamless switching from one port to the other is possible without interruption of the audio signal.

This also means that you can not use one physical {{< tooltip "Switch">}} and separate the {{< tooltip "Primary">}} and {{< tooltip "Secondary">}} traffic with different VLANs like you could do this with other audio network protocols. 

{{< figure src="/images/redundancy.drawio.svg" alt="Redundancy scheme in Milan networks">}}