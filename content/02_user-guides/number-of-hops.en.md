---
title: "Number of hops"
date: 2025-02-11
weight: 40
---

{{% notice info %}}
The maximum number of hops is dependant on the network speed.
- A 100Mbps network allows for max. 7 hops before it reaches the 2ms presentation time offset.
- A 1Gbps network allows for max. 14 hops before it reaches the 2ms presentation time offset.
{{% /notice %}}

A Milan AVB network is fully time-aware, meaning switches account for the worst-case residency time of a packet. Unlike other audio network protocols, Milan ensures that the required transmission time can be determined before a packet is sent. By configuring the {{< tooltip "Stream">}} {{< tooltip "PTO">}} in the {{< tooltip "Talker" >}}, it is possible to verify in advance whether a deadline can be met. 

Each transition a packet makes through a switch is known as a hop.

As a rule of thumb, the worst-case residency time for a packet in a switch is approximately 140µs on a 1Gbps network and 280µs on a 100Mbps network.

Milan specifies a latency limit of 2ms for guaranteed packet delivery. This allows for a maximum of 14 hops on a 1Gbps network and 7 hops on a 100Mbps network. As shown in [Fig. 1](#fig-number-of-hops-100Mbps) and [Fig. 2](#fig-number-of-hops-1000Mbps), fewer hops result in lower latency within a Milan network.

|                 | 100Mbps | 1Gbps |
|-----------------|-----------|---------|
| Latency per hop | 280µs | 140µs |
| Max. number of hops | 7 | 14 |

## Max. number of hops in a 100Mbps network

{{< figure src="/images/number_of_hops_100Mbps.drawio.svg" alt="Max. number of hops for 100Mbps" fig-num="1" title="Max. number of hops in a 100Mbps network: 7" id="fig-number-of-hops-100Mbps">}}

## Max. number of hops in a 1Gbps network

{{< figure src="/images/number_of_hops_1Gbps.drawio.svg" alt="Max. number of hops for 100Mbps" fig-num="2" title="Max. number of hops in a 1Gbps network: 14" id="fig-number-of-hops-1000Mbps">}}