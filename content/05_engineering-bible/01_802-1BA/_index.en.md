---
title: "802.1BA - AVB"
date: 2026-03-21
weight: 2
---

{{% notice info %}}
- AVB supports full duplex with speeds >= 100Mbps for Ethernet and EPON.
- Support for payloads up to 1500Byte. No support for Jumbo frames!
- SRClass A max. end-to-end latency: 2ms; SRClass B max. end-to-end latency: 50ms
- SRP and gPTP support required to form an AVB domain.
{{%/notice%}}

The IEEE 802.1BA specification defines the essential components of an {{< tooltip "AVB">}} network, ensuring seamless cooperation and interoperability for efficient and reliable audio and video stream transmission. It establishes how AVB-capable devices and switches can be integrated to deliver media with guaranteed timing and low latency.

Beyond standard Ethernet functionality, 802.1BA addresses challenges introduced by non-AV devices in the network, such as disruptions to timing, bandwidth allocation, and reliability. It specifies additional features, such as Traffic Classes and synchronization protocols, required for robust AVB operation, bridging the gaps left by other standards.

This specification serves as an umbrella document, referencing key AVB standards.

The most important definitions are:

## Supported data rates

{{< notice info >}}
{{< global_reference ref="IEEE8021BA">}}, Table 6-1
{{< /notice >}}


The 802.1BA specification defines the supported data rates for {{< tooltip "AVB">}} networks. Amongst others, these include:

- Ethernet, operating in full duplex mode, with a network speed of 100 Mbps or higher.
- Ethernet Passive Optical Network (EPON), which supports high-speed optical data transmission.

## Supported frame sizes

{{< notice info >}}
{{< global_reference ref="IEEE8021BA" clause="6.3" >}}
{{< /notice >}}

Because of the time-sensitive nature of an AVB network, frame sizes do matter. An AVB network supports payloads up to 1500 Byte. Larger payloads (e.g. Jumbo frames) are not supported.

## Stream Reservation Classes

There are two {{< tooltip "SRClasses" "SRClass">}} introduced: SRClass A and SRClass B. This classes are used to differentiate between latency requirements of a {{< tooltip "Stream">}} between a {{< tooltip "Talker">}} and a {{< tooltip "Listener">}}. For the technical details please refer to 
- TODO: Add reference.
- TODO: Explain concept of SRClass C

**NOTE:** The minimum end-to-end latency is defined by the number of hops between a Talker and a Listener. For more details, please refer to the [Number of hops](../../02_user-guides/number-of-hops.md) section.

| SR Class | Max. end-to-end latency |
|- |- |
| A        | 2ms                     |
| B        | 50ms                    |

## AVB domain


{{< notice info >}}
{{< global_reference ref="IEEE8021BA" clause="6.4" >}}
{{< /notice >}}

An AVB domain is defined as a connected set of devices that support {{< tooltip "SRP">}} with the same priority per {{< tooltip "SRClass" >}} furthermore they must support {{< tooltip "gPTP">}} (see [802.1AS](02_802-1AS)). This also means that a switch that is not AVB capable, can not be used to connect different AVB domains. This is depicted in [Fig.1](#fig-avb-boundaries).

{{< figure src="/images/avb_boundaries.drawio.svg" alt="Multiple AVB domains" fig-num="1" title="Multiple AVB domains" id="fig-avb-boundaries">}}
