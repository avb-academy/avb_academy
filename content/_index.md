---
title: "AVB Academy"
---

# Introduction

You are looking for information about the Milan protocol, and someone mentioned that you can find it at the AVB Academy. However, you might be wondering: why AVB Academy when you are interested in Milan? Before answering that question, let us take a step back. What forms the foundation of Milan?

{{% notice style="important" title="Subscribe to our newsletter" icon="fa-solid fa-envelope-circle-check" %}}
Want early access to the latest version of AVB Academy? Prefer occasional updates over inbox spam?  
[Click here to sign up to the newsletter](https://forms.gle/NvR2HfGVQesiAupG7)
{{% /notice %}}

## Introduction to Time-Sensitive Networking (TSN)

Time-Sensitive Networking (TSN) is a set of {{< tooltip "IEEE">}} standards that extend standard Ethernet to support real-time, deterministic communication. It enables guaranteed bandwidth, low latency, and synchronization for critical applications.

Audio Video Bridging (AVB) is a set of standards within the broader {{< tooltip "TSN">}} family, designed for professional audio and video transport. It was one of the first TSN profiles to be implemented, providing features such as:

- Stream reservation for guaranteed bandwidth: [Details about Stream reservation](01_milan/03_traffic-shaping/stream-reservation/_index.md)
- Precise time synchronization using {{< tooltip "gPTP">}}: [Details about timing](01_milan/00_network-timing/_index.md)
- Low-latency forwarding with credit-based traffic shaping: [Details about traffic shaping](01_milan/03_traffic-shaping/fqtss/_index.md)

## Milan: The ProAV Flavor of AVB

{{< tooltip "Milan">}} is a ProAV-specific {{< tooltip "AVB">}} solution developed by the {{< tooltip "Avnu Alliance">}}. It ensures interoperability by defining a deterministic and fully standardized network transport layer for professional audio and video devices.

{{% notice info %}}
This knowledge base dives deep into the technical details of {{< tooltip "Milan">}}, helping engineers and integrators get a solid understanding of how it works and what it offers. For a broader overview and high-level summary, you might want to visit [milanav.com](https://milanav.com).
{{% /notice %}}