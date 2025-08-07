---
title: "Forward Queuing for Time-Sensitive Streams (FQTSS)"
date: 2025-02-18
---

Milan utilizes {{< tooltip "FQTSS">}} to shape traffic. The approach is explained in detail below.

Switch ports are described based on the traffic direction for the current observation.  
- An {{< tooltip "ingress port" "Ingress port">}} describes traffic flowing into a switch.  
- An {{< tooltip "egress port" "Egress port">}} describes traffic flowing out of a switch. 

The following examples refer to the following setup: All three streams that enter at three different ports of a switch are forwarded to the remaining port.

{{< figure src="/images/traffic-shaping-routing.drawio.svg" alt="Example Routing of 3 Streams" fig-num="1" title="Example Routing of 3 Streams" id="fig-fqtss-routing" >}}

## Strict priority forwarding

The following figure shows all three streams from their resp. {{< tooltip "ingress port" "Ingress port">}} forwarded to the {{< tooltip "egress port" "Egress port">}} with considerung Strict Priority Schedulung only. The packets are forwarded according to their priority immediately. 

- **Time-critical:** packets have the highest priority.
- **Best-Effort:** packets have low priority.

Considering strict priority forwarding only leads to **time-critical** packets beeing forwarded always first when teh forwarding algorithm would have the choice between a **time-critical** and a **Best-Effort** packet.

This results in a blocking delay on lower-priority packets whenever high-priority packets are prioritized.

Due to the fact, that without traffic shaping, packets that ingress the switch almost simoultanously will be forwarded immediately, the combined resulting stream will have a bursty temporal structure.

{{< figure src="/images/traffic-shaping-strict-prio.drawio.svg" alt="Strict priority packet forwarding" fig-num="2" title="Strict Priority Packet Forwarding" id="fig-strict-prio" >}}


## Credit-based forwarding

Using the Credit-based Shaper additionally to Strict Priority Scheduling as shown in [Fig. 1](#fig-strict-prio), can one hand **shape** the resulting traffic stream into a uniformly distributed stream and on the other hand increase fairness towards lower priority traffic.

The core idea behind the Credit-based Shaper is simple:  
Each priority level has a **credit counter**.  
- It **decreases** when packets are being transmitted.  
- This counter **builds up** when packets are waiting to be sent.  

As soon as there is an opportunity to send data and the credit for a particular priority level is above zero, packets of that priority can be transmitted.

This approach spreads packet transmissions more evenly over time, reducing burstiness and smoothing traffic flow. Simoultanously lower priority traffic has the opportunity to be forwarded in the resulting gaps, when higher priority packet transmission is temporally not allowed due to a credit value lower than 0. In practice, the rate at which credit decreases (*sendSlope*) and increases (*idleSlope*) is calculated based on the amount of bandwidth that is reserved.

{{< figure src="/images/traffic-shaping-qav.drawio.svg" alt="Credit-based packet forwarding" fig-num="3" title="Credit-Based Packet Forwarding" id="fig-credit-based">}}
