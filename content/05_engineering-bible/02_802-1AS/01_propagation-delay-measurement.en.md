---
title: "Propagation Delay Measurement"
date: 2026-04-03
weight: 2
---

{{% notice info %}}
- The peer delay mechanism is used to measure the mean propagation delay between two network ports.
- The measured delay includes `PHY` and hardware delays, not only cable delay.
- Cable length cannot be derived directly from the measured propagation delay.
- Standard Ethernet switches exceed the allowed timing constraints of and are therefore not `asCapable`.
{{% /notice %}}

The peer delay mechanism is used to measure the propagation delay between two network ports. Each port performs the propagation delay measurement independently. Therefore, both link partners determine the link delay from their own perspective. The mechanism is depicted in [Fig. 1](#fig-propagation-delay-measurement):

{{< figure src="/images/propagation-delay-measurement.drawio.svg" alt="Propagation Delay Measurement using the Peer Delay Mechanism" fig-num="1" title="Propagation Delay Measurement using the Peer Delay Mechanism" id="fig-propagation-delay-measurement">}}

1. The initiator sends a `Pdelay_Req` message and generates timestamp {{< imath >}} t_1 {{< /imath >}}.
2. The responder receives the `Pdelay_Req` message and timestamps it with {{< imath >}} t_2 {{< /imath >}}.
3. The responder sends a `Pdelay_Resp` message and generates timestamp {{< imath >}} t_3 {{< /imath >}}.  
   The `Pdelay_Resp` message contains timestamp {{< imath >}} t_2 {{< /imath >}}.
4. Immediately after transmitting the `Pdelay_Resp` message, the responder sends a `Pdelay_Resp_Follow_Up` message containing timestamp {{< imath >}} t_3 {{< /imath >}}.
5. The initiator receives the `Pdelay_Resp` message and generates timestamp {{< imath >}} t_4 {{< /imath >}}.

Once all timestamps are available, the initiator can calculate the mean propagation delay {{< imath >}} D {{< /imath >}}:

<!-- IEEE802.1AS-2011, Eq. 11-1 -->
{{< math >}}
t_{ir} &= t_2 - t_1 \\
t_{ri} &= t_4 - t_3 \\
D &= \frac{t_{ir} + t_{ri}}{2} = \frac{(t_4 - t_1)-(t_3 - t_2)}{2}
{{< /math >}}

## Propagation Delay Calculation Example

Let us assume the following timestamps:

{{< math >}}
t_1 = 0,\quad t_2 = 100ns,\quad t_3 = 150ns,\quad t_4 = 250ns
{{< /math >}}

The mean propagation delay {{< imath >}} D {{< /imath >}} can be calculated as:

{{< math>}}
D &= \frac{(t_4 - t_1)-(t_3 - t_2)}{2} \\
&= \frac{(250ns - 0ns)-(150ns - 100ns)}{2} \\
&= \frac{250ns - 50ns}{2} \\ 
&= \frac{200ns}{2} \\ 
&= 100ns
{{< /math >}}

A signal in a copper cable typically propagates at approximately {{< imath >}} 0.6 \cdot c \text{ to } 0.7 \cdot c {{< /imath >}}, where {{< imath >}} c {{< /imath >}} denotes the speed of light with {{< imath >}} c = 299792458 \frac{m}{s} {{< /imath >}}.  
Using a velocity factor of {{< imath >}} 0.65 {{< /imath >}}, the corresponding length is:

{{< math >}}
l &= 100ns \cdot 0.65 \cdot 299792458 \frac{m}{s} \\
&\approx 19.49m
{{< /math >}}

## Interpretation and Practical Considerations

In this idealized example, the calculated delay corresponds to a cable length of approximately {{< imath >}} 20m {{< /imath >}}.

However, in real systems the measured propagation delay does not represent pure cable propagation delay. It also includes delays introduced by the {{< tooltip "PHYs" "PHY">}}, magnetics, and internal processing on both link partners. Therefore, the calculated length should be interpreted as an approximation and not as the actual physical cable length.

## NeighborPropDelayThresh and System Implications

As specified in {{< global_reference ref="MILANSpec" clause="4.2.6.1.1" >}}, the maximum value of `neighborPropDelayThresh` is set to {{< imath >}} 800ns {{< /imath >}} for copper-based links using 100BASE-TX and 1000BASE-T. The `neighborPropDelayThresh` is disabled for fiber-based connections.

Using the same calculation as above, this would correspond to a maximum cable length of:

{{< math>}}
l &= 800ns \cdot 0.65 \cdot 299792458 \frac{m}{s} \\
&\approx 155.9m
{{< /math >}}

At first glance, this exceeds the maximum allowed Ethernet cable length of {{< imath >}} 100m {{< /imath >}}.  
This discrepancy can be explained by the fact that the measured propagation delay includes not only the cable propagation delay, but also delays introduced by the {{< tooltip "PHYs" "PHY">}} and associated hardware on both link partners.

Typical {{< tooltip "PHY">}} delays are in the range of a few hundred nanoseconds per link, which accounts for a significant portion of the {{< imath >}} 800ns {{< /imath >}} threshold. As a result, the actual cable length is well within the specified Ethernet limits.

If the measured propagation delay exceeds {{< imath >}} 800ns {{< /imath >}}, the port is marked as not `asCapable` and therefore cannot participate in the AVB domain.

This also explains why standard Ethernet switches are not suitable for AVB networks. A typical store and forward switch introduces forwarding delays in the range of several microseconds, which significantly exceeds the allowed threshold. As a result, such links are classified as not asCapable.
