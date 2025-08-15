---
title: "Switches"
date: 2025-02-11
weight: 40
---

{{% notice info %}}

- The {{< tooltip "Switches" "Switch">}} are not included in the Milan specification - only {{< tooltip "Endstations" "Endstation">}} are. Therefore, {{< tooltip "Switches" "Switch">}} are AVB certified.
- Ingress port: Input port
- Egress port: Output port
{{% /notice %}}

AVB {{< tooltip "Switches" "Switch">}} do not require manual QoS configuration, as it is common with other Audio over IP protocols. With Milan, QoS configuration is automatically managed by the protocol. The fundamentals are detailed in [Stream Reservation Protocol (SRP)](../01_milan/03_traffic-shaping/stream-reservation/_index.en.md).

As mentioned in [Network Synchronization](../01_milan/00_network-timing/_index.en.md), one of the key advantages of a Milan network is that all participants share a common understanding of network time. This enables a fully deterministic transmission chain from the {{< tooltip "Talker" >}} to the {{< tooltip "Listener" >}}, allowing precise evaluation of whether a {{< tooltip "Delay">}} deadline can be met before the packet is sent. Unlike other audio network protocols on the market, Milan is the only one that guarantees full determinism, ensuring predictable and reliable audio transmission in all scenarios.

The AVB certification process ensures that all relevant features are supported by a switch. Therefore, only AVB-certified {{< tooltip "Switches" "Switch">}} are recommended for use in a Milan AVB network. A list of certified {{< tooltip "Switches" "Switch">}} is available on the Avnu website: [Certified Product Registry](https://avnu.org/certified-product-registry?cert=Network%20Device&type=).

When digging deeper in the functionality of a switch, it is important to understand that ports are defined based on the direction of the data flow under investigation: an ingress port serves as the input (mnemonic: ingress = input), while an egress port serves as the exit (mnemonic: egress = exit). For example, the traffic shaping mechanisms described in [Forward Queuing for Time-Sensitive Streams (FQTSS)](../01_milan/03_traffic-shaping/fqtss/_index.en.md) refer to the {{< tooltip "ingress" "Ingress port">}} and {{< tooltip "egress" "Egress port">}} port of a switch.