---
title: "Traffic shaping"
date: 2025-02-11
weight: 4
---

<!-- {{% notice info %}}
- The bounded latency of Milan AVB is ensured by using traffic shaping mechanisms.  
- The Stream Reservation Protocol (SRP) reserves only the required bandwidth for each stream, exclusively between the Talker and Listener. The remaining bandwidth stays available for other traffic.
- The Forward Queuing for Time-Sensitive Streams (FQTSS) ensures that packets are transmitted so that they reach their destination in time.  
- **Up to** 75% of the available bandwidth can be used for Milan traffic. If no stream requires the bandwidth, it is available for all other traffic.  
{{% /notice %}} -->

{{% notice info %}}
- Die garantierte Latenz von Milan AVB wird durch {{< termbase "Traffic Shaping">}} Mechanismen sichergestellt.
- Das {{< termbase "Stream Reservation Protocol">}} (SRP) reserviert nur die {{< termbase "Bandwidth">}} eines Streams auf dem Pfad zwischen Talker und Listener. Die übrige {{< termbase "Bandwidth">}} bleibt für anderen Netzwerkverkehr frei.
- Mit {{< termbase "Forward Queuing for Time-Sensitive Streams">}} (FQTSS) wird sichergestellt, dass Pakete pünktlich ihr Ziel erreichen.
- **Bis zu 75%** der verfügbaren {{< termbase "Bandwidth">}} können für Milan-Verkehr genutzt werden. Wird die Bandbreite nicht benötigt, steht sie allen anderen Datenströmen zur Verfügung.
{{% /notice %}}

<!-- {{< termbase "Traffic Shaping">}}  
{{< termbase "Traffic shaping">}}  
{{< termbase "traffic shaping">}}  
{{< termbase "traffic Shaping">}} -->

<!-- Traffic shaping is an essential part of Milan AVB and the biggest difference compared to other networked audio protocols. -->
{{< termbase "Traffic Shaping">}} ist ein zentraler Bestandteil von Milan AVB und macht den größten Unterschied zu anderen {{< termbase "Networked audio">}} Protokollen aus.

<!-- Two components are crucial for traffic shaping: -->
Für {{< termbase "Traffic Shaping">}} sind zwei Komponenten entscheidend:

<!-- 1. The [Stream Reservation Protocol](./stream-reservation/_index.md) (SRP) that configures a path from a Talker to a Listener.
2. The traffic shaper in a switch. The technology is based on the credit-based shaper and is often referred to as [Forwarding and Queuing for Time-Sensitive Streams](./fqtss/_index.md) (FQTSS). -->
1. Das [Stream Reservation Protocol](./stream-reservation/_index.md) (SRP), welches den Pfad zwischen {{< tooltip "Talker">}} und {{< tooltip "Listener">}} konfiguriert.
2. Der {{< termbase "Traffic Shaper">}} in einem {{< termbase "Switch">}}. Diese Technologie basiert auf dem {{< termbase "credit based">}} shaper und wird oft als [Forwarding and Queuing for Time-Sensitive Streams](./fqtss/_index.md) (FQTSS) bezeichnet.
