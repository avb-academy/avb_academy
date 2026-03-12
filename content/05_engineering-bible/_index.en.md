---
title: "Engineering Bible"
date: 2026-03-12
weight: 4
---

This section references the {{< tooltip "IEEE">}} specifications and gives a brief explanation to understand the most important underlying principles.

{{% notice info %}}
A lot of confusion arises from earlier stages of the AVB specification, when the specification was defined in different working groups. There was the 802.1Qav working group which defined the traffic shaping mechanisms. These mechanisms have been integrated into 802.1Q Clause 34 and are known as FQTSS. Furthermore, there was the 802.1Qat working group defining the Stream Reservation Protocol. This is now integrated into 802.1Q Clause 35 and known as SRP.  

Furthermore, specifications are updated regularly. This is indicated by adding a year to them. This page consciously does not this to not confuse first time readers. The referenced years can be found on the [Avnu Website](https://avnu.org/resource/milan-specification/).
{{% /notice %}}

| IEEE Standard | Defines                                               | Description   |
|-              |-                                                      |-              |
| 802.1BA       | {{< tooltip "AVB" >}}                                 | Audio Video Bridging (AVB) specification. <br> Defines profiles that specify the features, configurations, protocols, and procedures needed for bridges, stations, and LANs to transport time-sensitive audio and video streams. Details: 802.1BA<br>Further reading: [802.1BA](01_802-1BA)|
| 802.1AS       | {{< tooltip "gPTP">}}                                 | Generalized Precision Time Protocol (gPTP). <br> Specifies the protocol and procedures used to ensure that the synchronization requirements are met for time-sensitive applications. |
| 1722          | {{< tooltip "AVTP" >}}                                | Specifies the protocol, data encapsulations, and synchronization for interoperability between time-sensitive audio, video, and control applications using IEEE 802 Time-Sensitive Networking’s QoS capabilities.|
| 802.1Q        | {{< tooltip "FQTSS">}}<br>{{< tooltip "Qav" >}}       | Clause 34 defines the operation of Bridges that permit the definition, operation, and administration of Virtual LANs (VLANs) within Virtual Bridged Local Area Networks. |
| 802.1Q        | {{< tooltip "SRP" >}}<br>{{< tooltip "Qat">}}         | Clause 35 defines the Stream Reservation Mechanisms and signaling between ports. |       
| 1722.1        | {{< tooltip "ATDECC" >}}                              | AVB/TSN Discovery, Enumeration, Connection management, Control (ATDECC). <br> Specifies the protocol, device discovery, connection management, and control for interoperability between audio/video End Stations using {{< tooltip "AVTP">}} streams. |