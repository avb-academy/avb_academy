---
title: "Netzwerk-Hops"
date: 2025-02-11
weight: 40
---

<!-- {{% notice info %}}
The maximum number of hops is dependant on the network speed.
- A 100Mbps network allows for max. 7 hops before it reaches the 2ms presentation time offset.
- A 1Gbps network allows for max. 14 hops before it reaches the 2ms presentation time offset.
{{% /notice %}} -->
{{% notice info %}}
Maximale Anzahl an Netzwerk-Hops (abhängig von der Netzwerkgeschwindigkeit):
- 100 Mbps: max. 7 Hops bis zum Presentation Time Offset von 2 ms.
- 1 Gbps: max. 14 Hops bis zum Presentation Time Offset von 2 ms.
{{% /notice %}}

<!-- A Milan AVB network is fully time-aware, meaning switches account for the worst-case residency time of a packet. Unlike other audio network protocols, Milan ensures that the required transmission time can be determined before a packet is sent. By configuring the {{< tooltip "Stream">}} {{< tooltip "PTO">}} in the {{< tooltip "Talker" >}}, it is possible to verify in advance whether a deadline can be met. -->
Ein Milan AVB Netzwerk ist vollständig time-aware, das heißt, die {{< tooltip "Switches" "Switch" >}} berücksichtigen die Worst-Case-Aufenthaltszeit eines Pakets im Switch. Im Gegensatz zu anderen Audio-Netzwerkprotokollen stellt Milan sicher, dass die benötigte Übertragungszeit vor dem Versenden eines Pakets bestimmt werden kann. Durch die Konfiguration des {{< tooltip "Stream">}} {{< tooltip "PTO">}} im {{< tooltip "Talker" >}} lässt sich im Vorfeld überprüfen, ob eine Deadline eingehalten werden kann.

<!-- Each transition a packet makes through a switch is known as a hop. -->
Jede Weiterleitung eines Pakets durch einen Switch wird als Hop bezeichnet.

<!-- As a rule of thumb, the worst-case residency time for a packet in a switch is approximately 140µs on a 1Gbps network and 280µs on a 100Mbps network. -->
Als Faustregel gilt, dass die Worst-Case-Aufenthaltsdauer eines Pakets in einem Switch etwa 140 µs in einem 1 Gbps-Netzwerk und 280 µs in einem 100 Mbps-Netzwerk beträgt.

<!-- Milan specifies a latency limit of 2ms for guaranteed packet delivery. This allows for a maximum of 14 hops on a 1Gbps network and 7 hops on a 100Mbps network. As shown in [Fig. 1](#fig-number-of-hops-100Mbps) and [Fig. 2](#fig-number-of-hops-1000Mbps), fewer hops result in lower latency within a Milan network. -->
Milan legt ein Latenz-Limit von 2 ms für die garantierte Paketübertragung fest. Dadurch sind maximal 14 Hops in einem 1 Gbps-Netzwerk und 7 Hops in einem 100 Mbps-Netzwerk möglich. Wie in [Abb. 1](#fig-number-of-hops-100Mbps) und [Abb. 2](#fig-number-of-hops-1000Mbps) dargestellt, führt eine geringere Anzahl an Hops zu niedrigerer Latenz innerhalb eines Milan-Netzwerks.

<!-- |                 | 100Mbps | 1Gbps |
|-----------------|-----------|---------|
| Latency per hop | 280us | 140us |
| Max. number of hops | 7 | 14 | -->
|                     | 100 Mbps | 1 Gbps |
|---------------------|-----------|---------|
| Latenz pro Hop      | 280 µs    | 140 µs |
| Max. Anzahl an Hops | 7         | 14     |

<!-- ## Max. number of hops in a 100Mbps network -->
## Maximale Anzahl an Hops in einem 100 Mbps-Netzwerk

<!-- {{< figure src="/images/number_of_hops_100Mbps.drawio.svg" alt="Max. number of hops for 100Mbps" fig-num="1" title="Max. number of hops in a 100Mbps network: 7" id="fig-number-of-hops-100Mbps">}} -->
{{< figure src="/images/number_of_hops_100Mbps.drawio.svg" alt="Max. Anzahl Hops in einem 100Mbps-Netzwerk" fig-num="1" title="Maximale Anzahl an Hops in einem 100Mbps-Netzwerk: 7" id="fig-number-of-hops-100Mbps">}}

<!-- ## Max. number of hops in a 1Gbps network -->
## Maximale Anzahl an Hops in einem 1 Gbps-Netzwerk

<!-- {{< figure src="/images/number_of_hops_1Gbps.drawio.svg" alt="Max. number of hops for 1Gbps" fig-num="2" title="Max. number of hops in a 1Gbps network: 14" id="fig-number-of-hops-1000Mbps">}} -->
{{< figure src="/images/number_of_hops_1Gbps.drawio.svg" alt="Max. Anzahl Hops in einem 1Gbps-Netzwerk" fig-num="2" title="Maximale Anzahl an Hops in einem 1Gbps-Netzwerk: 14" id="fig-number-of-hops-1000Mbps">}}
