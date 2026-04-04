---
title: "Propagation Delay Measurement"
date: 2026-04-03
weight: 2
---

- Two step clock
- Point to point measurement of each port. Therefore, both ports will know the propagation delay

{{< figure src="/images/peer-delay-measurement.drawio.svg" alt="Peer Delay Measurement" fig-num="1" title="Peer Delay Measurement" id="fig-peer-delay-measurement">}}

## Measurement process

The measurement process depicted in [Fig. 1](#fig-peer-delay-measurement) shows the following steps:

1. The initiator starts by sending out a Pdelay_Req message and generating timestamp {{< imath >}} t_1 {{< /imath >}}.
2. The responder receives the Pdelay_Req message and timestamps it with {{< imath >}} t_2 {{< /imath >}}.
3. The responder sends a Pdelay_Resp message and timestamps it with {{< imath >}} t_3 {{< /imath >}}.  
    The returned Pdelay_Resp message also contains timestamp {{< imath >}} t_2 {{< /imath >}}.
4. Imediately after sending the Pdelay_Resp message, a Pdelay_Resp_Follow_Up message is sent which contains the timestamp {{< imath >}} t_3 {{< /imath >}}.
5. The initiator generates timestamp {{< imath >}} t_4 {{< /imath >}}.

Now, that all timestamps are available the initiator can calculate the mean propagation delay {{< imath >}} D {{< /imath>}}:
<!-- IEEE802.1AS-2011, Eq. 11-1 -->
{{< math >}}
t_{ir} &= t_2 - t_1 \\
t_{ri} &= t_3 - t_4 \\
D &= \frac{t_{ir} + t_{ri}}{2} = \frac{(t_4 - t_1)-(t_3 - t_2)}{2} \\
\frac{}{}
{{< /math >}}

t1 = 0  
t2 = 100ns  
t3 = 150ns  
t4 = 250ns  

{{< math >}}
D &= \frac{(t_4 - t_1)-(t_3 - t_2)}{2} \\
&= \frac{(250ns - 0ns)-(150ns - 100ns)}{2} \\ 
&= \frac{250ns - 50ns}{2} \\ 
&= \frac{200ns}{2} \\ 
&= 100ns
{{< /math >}}

100ns * 0.8 * c = 24m

--> PDelayThreshold (neighborPropDelayThresh) for copper: 800ns 
