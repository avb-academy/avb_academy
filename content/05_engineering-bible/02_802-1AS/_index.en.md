---
title: "802.1AS - gPTP"
date: 2026-03-21
weight: 3
---

{{% notice info %}}
- gPTP is limited to layer 2
{{% /notice %}}

The Milan specification uses the generalized Precision Timing Protocol (gPTP) to synchronize all particpants in the network. As already introduced in [Network Synchronization](01_milan/00_network-timing/), this section describes how all participants in the network share a common understanding of time. This is not to be confused with the Media Clock which is described in Sec. TODO.

The IEEE 802.1AS specification defines a mechanism to synchronize devices in a network so that time-sensitive applications can be deployed on such a network. The 802.1AS specification is called generalized Precision Timing Protocol (gPTP). It is a constrained subset of the IEEE 1588-2008 which is called Precision Timing Protocol version 2 (PTPv2).

While there are many details and specifics to this protocol it can be even more generalized (pun intended) by making the following assumptions:

- During startup of connected devices or if a new device is added to the network, all connected devices elect a Grand Master (GM) by applying the rules of the Best Time Transmitter Clock Algorithm (BTCA).
- Once the GM has been elected, it provides its time as an absolute reference to all connected devices in a gPTP domain.
- While  being in operation, all connected devices constantly synchronize their time to the time of the GM. This is done on a port to port basis which minimizes the influence of other network traffic and jitter.
- The gPTP traffic is considered management traffic and therefore not applied to any {{< tooltip "SRClass">}}. Inside a switch it has a higher priority than {{< tooltip "SRClassA">}} traffic.

## Frame

Frames are big. TODO: Find a way to visualize them. See: Sec. 10.5

## General

gPTP consists of three main messages:

- Announce Messages: Each device sends out its own Announce Message which is used to determine the Clock Leader. The Clock Leader election is described in detail in the [Best TimeTransmitter Clock Algorithm](00_btca) section.  

The Peer Delay measurement process uses three different messages to communicate on a port to port basis: {{< tooltip "Pdelay_Req">}}, {{< tooltip "Pdelay_Resp">}}, {{< tooltip "Pdelay_Resp_Follow_Up">}}. A detailed description of how these messages are used can be found in in the [Peer Delay Measurement Section](01_peer-delay-measurement.md).

## Synchronisation

gPTP is used to synchronize all network participants to a common time. The first step is always to determine a GrandMaster (GM). The election process is based on the clock parameters that each potential {{< tooltip "GM">}} is sending to the network. A detailed description can be found in the [Best TimeTransmitter Clock Algorithm](00_btca) section.

The transmission delay through a switch is compensated by the clock mechanism itself. Therefore, a synchronisation of two connected ports is necessary. The detailed description of the measurement process can be found in [Peer Delay Measurement](01_peer-delay-measurement).