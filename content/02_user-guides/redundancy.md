---
title: "Redundancy"
date: 2025-02-11
---

Redundancy is an optional feature in Milan. Therefore, not all Milan devices support redundancy.

If a Milan network is made redundant it has to be with physically separate networks. This means that you need a separate switches for the primary network and the secondary network. The reason for the pyhsical separation is in the protocol of how Milan works. The Milan network requires a separate {{< tooltip "gPTP">}} GrandMaster on each network. 

This also means that you can not use on physical switch and separate the primary and secondary traffic with different VLANs.

{{< figure src="/images/redundancy.drawio.svg" alt="Redundancy scheme in Milan networks">}}