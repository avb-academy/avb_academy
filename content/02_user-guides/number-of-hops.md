---
title: "Number of hops"
date: 2025-02-11
---

{{% notice info %}}
The maxiumum number of hops is dependant on the network speed.
- A 100Mbit network allows for max. 7 hops before it reaches the 2ms presentation time offset.
- A 1Gbit network allows for max. 14 hops before it reaches the 2ms presentation time offset.
{{% /notice %}}

A Milan network is fully time-aware, meaning switches account for the worst-case residency time of a packet. Unlike other audio network protocols, Milan ensures that the required transmission time can be determined before a packet is sent. By configuring the {{< tooltip "Stream">}} {{< tooltip "Delay">}} in the {{< tooltip "Talker" >}}, it is possible to verify in advance whether a deadline can be met. 

Each transition a packet makes through a switch is known as a hop.

As a rule of thumb, the worst-case residency time for a packet in a switch is approximately 140µs on a 1Gbit/s network and 280µs on a 100Mbit/s network.

Milan specifies a latency limit of 2ms for guaranteed packet delivery. This allows for a maximum of 14 hops on a 1Gbit/s network and 7 hops on a 100Mbit/s network. As shown in [Fig. 1](#fig-number-of-hops-100Mbps) and [Fig. 2](#fig-number-of-hops-1000Mbps), fewer hops result in lower latency within a Milan network.

|                 | 100Mbit/s | 1Gbit/s |
|-----------------|-----------|---------|
| Latency per hop | 280us | 140us |
| Max. number of hops | 7 | 14 |

## Max. number of hops in a 100Mbit/s network

{{< figure src="/images/number_of_hops_100Mbps.drawio.svg" alt="Max. number of hops for 100Mbit/s" fig-num="1" title="Max. number of hops in a 100Mbit/s network: 7" id="fig-number-of-hops-100Mbps">}}

## Max. number of hops in a 1Gbit/s network

{{< figure src="/images/number_of_hops_1Gbps.drawio.svg" alt="Max. number of hops for 100Mbit/s" fig-num="2" title="Max. number of hops in a 1Gbit/s network: 14" id="fig-number-of-hops-1000Mbps">}}