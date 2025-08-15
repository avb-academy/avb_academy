---
title: "Milan Myths"
date: 2025-08-04
weight: 3
---

There are several persistent myths surrounding Milan and its foundational technology, AVB.

This page addresses the most common misconceptions with clear, technically accurate explanations.

- [Myth: AVB is obsolete](#myth-avb-is-obsolete)
- [Myth: Milan is proprietary](#myth-milan-is-proprietary)
- [Myth: Milan is old and outdated](#myth-milan-is-old-and-outdated)
- [Myth: Milan always has a latency of 2ms](#myth-milan-always-has-a-latency-of-2ms)
- [Myth: There are no AVB-capable switches available](#myth-there-are-no-avb-capable-switches-available)
- [Myth: Milan always blocks 75% of the available network bandwidth](#myth-milan-blocks-75-of-the-available-network-bandwidth)
- [Myth: Milan control is still under development](#myth-milan-control-is-still-under-development)

{{% notice info %}}  
This page assumes you are familiar with the relationship between AVB and Milan.  
For a brief overview, see the [AVB Academy introduction](../_index.en.md).  
{{% /notice %}}

---

<a id="myth-avb-is-obsolete"></a>
{{% notice style="warning" title="Myth: AVB is obsolete" icon="fa-solid fa-circle-question"%}}
It is often claimed that AVB is obsolete because the IEEE AVB working group ended its activities in 2012 when it was renamed into the Time-Sensitive Networking (TSN) task group to focus on industrial applications.
{{% /notice %}}

{{% notice style="tip" title="Reality: AVB is very much alive" icon="fa-solid fa-circle-check"%}}
The AVB specification (IEEE 802.1BA) is still active and maintained, with the latest revision published in 2021. The renaming of the working group reflected an expanded scope, not a move away from AVB.

Audio and video transport remains a core use case within TSN, alongside newer applications in industrial automation, automotive, and aerospace. Rather than being obsolete, AVB has evolved within a broader standards family.
{{% /notice %}}

---

<a id="myth-milan-is-old-and-outdated"></a>
{{% notice style="warning" title="Myth: Milan is old and outdated" icon="fa-solid fa-circle-question"%}}
Milan is sometimes perceived as a legacy solution that has been surpassed by newer, IP-based audio networking technologies.

See also: [Myth: AVB is obsolete](#myth-avb-is-obsolete)
{{% /notice %}}

{{% notice style="tip" title="Reality: Milan is one of the most modern audio networking standards" icon="fa-solid fa-circle-check"%}}
Milan is actually among the most recent professional audio networking standards. It was first released in 2018, while widely adopted IP-based standards like AES67 date back to 2013.

More importantly, Milan provides deterministic performance and precise timing that IP-based solutions still struggle to match. It combines Ethernet transport with guaranteed delivery and bounded latency, making it ideal for high-performance audio applications.
{{% /notice %}}

---

<a id="myth-milan-is-proprietary"></a>
{{% notice style="warning" title="Myth: Milan is a proprietary protocol" icon="fa-solid fa-circle-question"%}}
Some claim that Milan is a proprietary protocol, used exclusively by a selected group of ProAV manufacturers.
{{% /notice %}}

{{% notice style="tip" title="Reality: Milan is based on open IEEE standards" icon="fa-solid fa-circle-check"%}}
Milan is not proprietary. It is a clearly defined, open specification built on top of IEEE open standards including 802.1AS (time synchronization), 802.1Q (traffic shaping), 1722 (streaming transport), and 1722.1 (device discovery and control).

The Milan protocol is developed collaboratively by leading ProAV manufacturers within the Avnu Alliance, ensuring it meets the real-world needs of professional users. Any manufacturer can implement Milan without licensing fees, and the full specification is freely available from the [Avnu Alliance website](https://avnu.org/resource/milan-specification/).
{{% /notice %}}

---

<a id="myth-milan-always-has-a-latency-of-2ms"></a>

{{% notice style="warning" title="Myth: Milan always has a latency of 2ms" icon="fa-solid fa-circle-question"%}}
Because AVB networks originally introduced a default latency of 2ms, some believe this is the fixed or only possible latency for Milan systems.
{{% /notice %}}

{{% notice style="tip" title="Reality: Milan guarantees a bounded latency, not a fixed one" icon="fa-solid fa-circle-check"%}}
Milan networks are fully time-aware. All devices, including switches, share a synchronized understanding of time. This enables them to calculate and guarantee precise end-to-end transmission delays.

As a result, Milan can guarantee a minimum playout delay tailored to the specific path and stream characteristics. Typical configurations range from 0.25 ms to 2 ms.
{{% /notice %}}


---

<a id="myth-there-are-no-avb-capable-switches-available"></a>
{{% notice style="warning" title="Myth: There are no AVB-capable switches available" icon="fa-solid fa-circle-question"%}}
It is often claimed that Milan is impractical because it requires specialized switches, and that mainstream networking vendors no longer support AVB.
{{% /notice %}}

{{% notice style="tip" title="Reality: Certified AVB switches are widely available" icon="fa-solid fa-circle-check"%}}
AVB-capable switches incorporate advanced Ethernet technologies such as the Precision Time Protocol v2 (PTPv2) for precise clock synchronization. Additionally, they implement traffic shaping and bandwidth reservation mechanisms defined by the AVB standards to guarantee bounded latency and deterministic delivery of audio streams.

A wide range of manufacturers produce certified AVB switches, including Netgear, Cisco, Extreme Networks, Luminex, Niveo Professional, Adamson Systems Engineering, d&b audiotechnik, L-Acoustics, and others. The ecosystem continues to expand with new certified products regularly introduced.

You can find the current list of certified switches in the Avnu Alliance [Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Network%20Device).
{{% /notice %}}

---

<a id="myth-milan-blocks-75-of-the-available-network-bandwidth"></a>
{{% notice style="warning" title="Myth: Milan always blocks 75% of the available network bandwidth" icon="fa-solid fa-circle-question"%}}
There is a persistent belief that Milan blocks 75% of the network bandwidth, severely limiting other traffic.
{{% /notice %}}

{{% notice style="tip" title="Reality: Your network is not 75% full by default" icon="fa-solid fa-circle-check"%}}
Milan uses bandwidth reservation to guarantee time-sensitive delivery, but only reserves the bandwidth required by each stream. For example, an 8-channel stream at 48 kHz reserves around 17 Mbps.

All remaining bandwidth is available for other traffic. The 75% figure refers to the maximum possible reservation (based on AVB Class A and B limits), not the typical usage. You can find a detailed calculation in the description of the [Stream Reservation Protocol](../01_milan/03_traffic-shaping/stream-reservation/_index.en.md).
{{% /notice %}}

---

<a id="myth-milan-control-is-still-under-development"></a>
{{% notice style="warning" title="Myth: Milan control is still under development" icon="fa-solid fa-circle-question"%}}
It is sometimes assumed that Milan control is incomplete or still evolving, making it unsuitable for real-world deployment.
{{% /notice %}}

{{% notice style="tip" title="Reality: Milan control is fully defined and standardized" icon="fa-solid fa-circle-check"%}}
Milan uses the ATDECC protocol (defined in IEEE 1722.1) for control, which defines standardized mechanisms for device discovery, enumeration, and stream management.

These control capabilities have been part of the Milan specification since its initial release and are already implemented in certified Milan devices.
{{% /notice %}}
