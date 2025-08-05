---
title: "Milan AVB Myths"
date: 2025-08-04
weight: 3
---

There are several persistent myths surrounding Milan and its underlying technology, AVB.

This page addresses the most common misconceptions with clear, technically accurate explanations to help clarify how these technologies actually work.

- [Myth: AVB is obsolete](#myth-avb-is-obsolete)
- [Myth: There are no AVB-capable switches available](#myth-there-are-no-avb-capable-switches-available)
- [Myth: Milan control is still under development](#myth-milan-control-is-still-under-development)
- [Myth: Milan AVB is old and outdated](#myth-milan-is-old-and-outdated)
- [Myth: Milan AVB blocks 75% of the available network bandwidth](#myth-avb-milan-uses-75-of-the-available-network-bandwidth)

---

<a id="myth-avb-is-obsolete"></a>
{{% notice style="warning" title="Myth: AVB is obsolete" icon="fa-solid fa-circle-question"%}}
Some claim that AVB is obsolete because the IEEE AVB working group ended its activities in 2012, when it was renamed the Time-Sensitive Networking (TSN) task group to focus on industrial applications.

{{% /notice %}}
{{% notice style="tip" title="Reality: AVB is very much alive" icon="fa-solid fa-circle-check"%}}

While the IEEE AVB working group was renamed to the TSN Task Group in 2012, this was due to an expansion of scope, not a shift away from AVB. The AVB specification (IEEE 802.1BA) is still active and maintained, with the latest revision published in 2021.

Audio and video transport remains a foundational use case within TSN, alongside emerging applications in industrial automation, automotive, and aerospace. Rather than being obsolete, AVB has evolved as part of a broader set of time-sensitive networking standards.
{{% /notice %}}

---
<a id="myth-there-are-no-avb-capable-switches-available"></a>
{{% notice style="warning" title="Myth: There are no AVB-capable switches available" icon="fa-solid fa-circle-question"%}}

Milan AVB is often said to lack traction because it only works with dedicated switches, and mainstream networking manufacturers no longer support it.

{{% /notice %}}

{{% notice style="tip" title="Reality: Certified AVB switches are widely available" icon="fa-solid fa-circle-check"%}}

AVB-capable switches are actively developed and sold by a wide range of manufacturers. Certified products are available from Netgear, Cisco, Extreme Networks, Luminex, Niveo Professional, Adamson Systems Engineering, L-Acoustics, d&b audiotechnik, and others. New certified devices continue to be introduced as the AVB ecosystem grows.

You can find the current list of certified switches in the Avnu Alliance [Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Network%20Device).

{{% /notice %}}

---

<a id="myth-milan-control-is-still-under-development"></a>
{{% notice style="warning" title="Myth: Milan control is still under development" icon="fa-solid fa-circle-question"%}}

It is often assumed that Milan control is incomplete or still being developed, making it unsuitable for real-world deployment.
{{% /notice %}}
{{% notice style="tip" title="Reality: Milan control is fully defined and standardized" icon="fa-solid fa-circle-check"%}}

The mechanisms for controlling Milan devices have been clearly defined since the first release of the Milan specification. Milan relies on the ATDECC protocol (from IEEE 1722.1), which provides standardized support for device discovery, enumeration, and stream connection management.

These control features are already implemented in certified Milan devices and form an integral part of the Milan ecosystem.
{{% /notice %}}

---
<a id="myth-milan-is-old-and-outdated"></a>
{{% notice style="warning" title="Myth: Milan is old and outdated" icon="fa-solid fa-circle-check"%}}

Milan AVB is sometimes perceived as legacy technologies that have been surpassed by newer, IP-based audio networking solutions.

See also: [Myth: AVB is obsolete](#myth-avb-is-obsolete)
{{% /notice %}}
{{% notice style="tip" title="Reality: Milan is one of the most modern audio networking standards" icon="fa-solid fa-circle-question"%}}

Among current audio-over-IP technologies, Milan is actually one of the most recent specifications. It was first released in 2018. In contrast, the most widely adopted IP-based standard, AES67, was published in 2013.

More importantly, none of the existing IP-based solutions offer the same level of determinism and timing precision as Milan. It combines the benefits of Ethernet-based transport with guaranteed performance, making it ideally suited for professional audio applications where timing and reliability are critical.
{{% /notice %}}

---

<a id="myth-avb-milan-uses-75-of-the-available-network-bandwidth"></a>
{{% notice style="warning" title="Myth: Milan AVB blocks 75% of the available network bandwidth" icon="fa-solid fa-circle-check" %}}

There is a persistent belief that AVB/Milan reserves 75% of the network bandwidth, severely limiting other traffic.

{{% /notice %}}

{{% notice style="tip" title="Reality: Your network is not 75% full" icon="fa-solid fa-circle-question" %}}

AVB/Milan uses bandwidth reservation to guarantee performance, but only reserves what each stream actually needs. For example, an 8-channel stream at 48 kHz reserves around 17 Mbps. This bandwidth is reserved exclusively to ensure time-sensitive delivery with guaranteed bounded latency.

All unreserved bandwidth remains fully available to other traffic. You can find a detailed bandwidth calculation in the description of the [Stream Reservation Protocol](../01_milan/03_traffic-shaping/stream-reservation/_index.md).

{{% /notice %}}


