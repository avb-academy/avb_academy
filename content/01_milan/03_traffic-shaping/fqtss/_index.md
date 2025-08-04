---
title: "Forward Queuing for Time-Sensitive Streams (FQTSS)"
date: 2025-02-18
---

Milan utilizes {{< tooltip "FQTSS">}} to shape traffic. The approach is explained in detail below.

Switch ports are described based on the traffic direction for the current observation.  
- An {{< tooltip "ingress port" "Ingress port">}} describes traffic flowing into a switch.  
- An {{< tooltip "egress port" "Egress port">}} describes traffic flowing out of a switch.  

## Strict priority forwarding

Consider the example shown in the figure below.

This figure illustrates an example of three {{< tooltip "ingress port" "Ingress port">}} with packets that are all sent to the same {{< tooltip "egress port" "Egress port">}}. The prioritization of packets is as follows:

- **Time-critical:** packets have the highest priority.
- **Less critical:** packets have medium priority.
- **Legacy:** packets have low priority.

In strict priority forwarding, **time-critical** packets are always forwarded first, preventing lower-priority packets from being transmitted as long as high-priority packets remain in the transmission queue. This results in a blocking effect on lower-priority packets whenever high-priority packets are present at an {{< tooltip "ingress port" "Ingress port">}} that needs to forward packets to an {{< tooltip "egress port" "Egress port">}}.

{{< figure src="/images/traffic-shaping-strict-prio.drawio.svg" alt="Strict priority packet forwarding" fig-num="1" title="Strict Priority Packet Forwarding" id="fig-strict-prio" >}}


## Credit-based forwarding

The blocking effect of strict priority forwarding as shown in  [Fig. 1](#fig-strict-prio) can be mitigated using a credit-based shaper. To keep this example straightforward, we will focus only on **time-critical** and **less critical** packets, leaving out **legacy** packet behavior for simplicity.

The core idea behind the credit-based shaper is simple:  
Each priority level has a **credit counter**.  
- This counter **builds up** when packets are waiting to be sent.  
- It **decreases** when packets are being transmitted.  

As soon as there is an opportunity to send data and the credit for a particular priority level is above zero, packets of that priority can be transmitted.

This approach spreads packet transmissions more evenly over time, reducing burstiness and smoothing traffic flow. **In this example**, we assume that when a packet is being transmitted, the credit decreases **twice as fast** as it builds up when waiting for a transmission opportunity. In practice, the rate at which credit decreases (*sendSlope*) and increases (*idleSlope*) is calculated based on the amount of bandwidth that is reserved.

{{< figure src="/images/traffic-shaping-qav.drawio.svg" alt="Credit-based packet forwarding" fig-num="2" title="Credit-Based Packet Forwarding" id="fig-credit-based">}}

