---
title: "802.1AS - gPTP"
date: 2026-03-21
weight: 3
---

{{% notice info %}}
- gPTP is limited to layer 2
{{% /notice %}}

The Milan specification uses the generalized Precision Timing Protocol (gPTP) to synchronize all particpants in the network. As already introduced in [Network Synchronization](01_milan/00_network-timing/), this section describes how all participants in the network share a common understanding of time. This is not to be confused with the Media Clock which is described in Sec. TODO: Reference Media Clock section in 1722 chapter.

The IEEE 802.1AS specification defines a mechanism to synchronize devices in a network so that time-sensitive applications can be deployed on such a network. The 802.1AS specification is called generalized Precision Timing Protocol (gPTP). It is a constrained subset of the IEEE 1588-2008 which is called Precision Timing Protocol version 2 (PTPv2).

While there are many details and specifics to this protocol it can be even more generalized (pun intended) by making the following assumptions:

- During startup of connected devices or if a new device is added to the network, all connected devices elect a Grand Master (GM) by applying the rules of the Best Time Transmitter Clock Algorithm (BTCA).
- Once the {{< tooltip "GM">}} has been elected, it provides its time as an absolute reference to all connected devices in a {{< tooltip "gPTP" >}} domain.
- While  being in operation, all connected devices constantly synchronize their time to the time of the {{< tooltip "GM">}}. This is done on a port to port basis which minimizes the influence of other network traffic and jitter.
- The {{< tooltip "gPTP" >}} traffic is considered management traffic and therefore not applied to any {{< tooltip "SRClass">}}. Inside a switch it has a higher priority than {{< tooltip "SRClassA">}} traffic.

## Frame

Frames are big. TODO: Find a way to visualize them. See: Sec. 10.5

## General

gPTP consists of three main messages:

- Announce Messages: Each device sends out its own Announce Message which is used to determine the Clock Leader. The Clock Leader election is described in detail in the [Best TimeTransmitter Clock Algorithm](00_btca) section.  

- The Propagation Delay measurement process uses three different messages to communicate on a port to port basis: {{< tooltip "Pdelay_Req">}}, {{< tooltip "Pdelay_Resp">}}, {{< tooltip "Pdelay_Resp_Follow_Up">}}. A detailed description of how these messages are used can be found in in [Propagation Delay Measurement](01_propagation-delay-measurement.md).


## The same time everywhere

To understand better how gPTP is actually used to synchronize devices, we need to extend our timing vocabulary. It is important to understand that we distinguish between Syntonization and Synchronisation. The term Syntonization means that all clocks in a system run at the same rate. While the term Synchronization describes clocks that run on the same time origin (phase/epoch).  
A clock has two indpenedent property:

- Frequency: Describes how fast time advances. Example: Does on local second equal on GM second?
- Phase: What time the clock currently shows. Example: Is it currently 12:00:00:000000000 or is it 12:00:00:000000500?

Clocks that show different times (e.g. clock A: 12:00:00 and clock B: 12:00:05) but advance perfectly together are syntonized but not synchronized because they differ by 5s.

### GM time

GM does not sent an absolute time but a message (Sync message?) that contains the information: At this instant this Sync Message left me, my clock reads 12:00:00.  
The receiving node then tries to answer the question: When that sync message arrived here, my local clock showed which time?    
From the time the sync message left the GM and the time it received the message it can derive an offset: {{< imath >}} \text{offset} = \text{GM time} - \text{local time}{{< /imath >}}. But this can only work if the node also knows the propagation delay, the residence time corrections and the frequency relationship.

### Syntonization

Suppose that the GM clock frequency runs perfectly. The slave clock runs slightly faster.

- GM frequency: 100MHz
- Slave frequency: 100.1MHz

If both devices start at the same time, the slave clock will drift away from the GM time. Therefore, syntonization is crucial so that all devices advance time in the similar manner.


### Synchronisation

The synchronisation requires that the clock frequencies are aligned first before you can align the phase, so that all clocks show the same time all the time.


## Timing Layers

### Election

BMCA selects the GM

### Frequency alignment (Syntonization)

Neighbor clocks continuously measure relative frequency to each other (on each port). 

### Delay characterization

Each link measures the propagation delay --> link to 01_prop

### Time alignment (Synchronization)

Using 

- Sync timestamps
- Delay corrections
- Frequency corrections

A synchronized slave clock is a clock whose local oscillator has been frequency-corrected to run at the same rate as the grandmaster and whose local time value is continuously phase-corrected so that it represents the estimated current grandmaster time.

---

gPTP is used to synchronize all network participants to a common time. The first step is always to determine a GrandMaster (GM). The election process is based on the clock parameters that each potential {{< tooltip "GM">}} is sending to the network. A detailed description can be found in the [Best TimeTransmitter Clock Algorithm](00_btca) section.

The transmission delay through a switch is compensated by the clock mechanism itself. Therefore, a synchronisation of two connected ports is necessary. The detailed description of the measurement process can be found in [Propagation Delay Measurement](01_propagation-delay-measurement).