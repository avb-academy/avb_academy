---
title: "AVB Myths"
date: 2025-08-04
weight: 3
---

There are several persistent myths surrounding Milan and its underlying technology, AVB.

This page addresses the most common misconceptions with clear, technically accurate explanations to help clarify how these technologies actually work.

- [Myth: AVB is obsolete](#myth-avb-is-obsolete)
- [Myth: There are no AVB-capable switches available](#myth-there-are-no-avb-capable-switches-available)
- [Myth: Milan control is still under development](#myth-milan-control-is-still-under-development)
- [Myth: Milan is old and outdated](#myth-milan-is-old-and-outdated)

---

## Myth: AVB is obsolete

Some claim that AVB is obsolete because the IEEE AVB working group ended its activities in 2012, when it was renamed the Time-Sensitive Networking (TSN) task group to focus on industrial applications.

### Reality: AVB is very much alive

This is a misconception. While the IEEE AVB working group was renamed to the TSN Task Group in 2012, this was due to an expansion of scope, not a shift away from AVB. The AVB specification (IEEE 802.1BA) is still active and maintained, with the latest revision published in 2021.

Audio and video transport remains a foundational use case within TSN, alongside emerging applications in industrial automation, automotive, and aerospace. Rather than being obsolete, AVB has evolved as part of a broader set of time-sensitive networking standards.

---

## Myth: There are no AVB-capable switches available

AVB is said to lack traction because it only works with dedicated network switches, and manufacturers of standard networking equipment no longer support it.

### Reality: Certified AVB switches are widely available

This claim does not reflect the current market. Multiple manufacturers actively provide AVB-certified switches, and new products continue to appear. Vendors such as Luminex, Netgear, and Cisco offer certified devices, and others are part of the growing ecosystem.

You can find the up-to-date list of certified devices in the Avnu Alliance [Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Network%20Device).

---

## Myth: Milan control is still under development

It is often assumed that Milan control is incomplete or still being developed, making it unsuitable for real-world deployment.

### Reality: Milan control is fully defined and standardized

This assumption is incorrect. The mechanisms for controlling Milan devices have been clearly defined since the first release of the Milan specification. Milan relies on the ATDECC protocol (from IEEE 1722.1), which provides standardized support for device discovery, enumeration, and stream connection management.

These control features are already implemented in certified Milan devices and form an integral part of the Milan ecosystem.

---

## Myth: Milan is old and outdated

AVB and Milan are sometimes perceived as legacy technologies that have been surpassed by newer, IP-based audio networking solutions.

See also: [Myth: AVB is obsolete](#myth-avb-is-obsolete)

### Reality: Milan is one of the most modern audio networking standards

This perception is incorrect. Among current audio-over-IP technologies, Milan is actually one of the most recent specifications—first released in 2018. In contrast, the most widely adopted IP-based standard, AES67, was published in 2013.

More importantly, none of the existing IP-based solutions offer the same level of determinism and timing precision as Milan. It combines the benefits of Ethernet-based transport with guaranteed performance, making it ideally suited for professional audio applications where timing and reliability are critical.
