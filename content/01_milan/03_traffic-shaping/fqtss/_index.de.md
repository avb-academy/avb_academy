---
title: "Forward Queuing for Time-Sensitive Streams (FQTSS)"
date: 2025-02-18
---

<!-- Milan AVB utilizes {{< tooltip "FQTSS">}} to shape traffic. The approach is explained in detail below. -->
Milan AVB nutzt {{< tooltip "FQTSS">}} für das {{< termbase "Traffic Shaping">}}. "Forward Queuing" lässt sich auf Deutsch mit "Warteschlangenspeicher" übersetzen. 

<!-- Switch ports are described based on the traffic direction for the current observation. -->
Die Switch-Ports werden je nach Richtung des aktuellen Datenverkehrs beschrieben.

<!-- - An {{< tooltip "ingress port" "Ingress port">}} describes traffic flowing into a switch.
- An {{< tooltip "egress port" "Egress port">}} describes traffic flowing out of a switch. -->
- Ein {{< tooltip "Ingress Port">}} beschreibt den Datenverkehr, der in einen Switch hineinfließt. Auf Deutsch: {{< termbase "Ingress port">}}  
- Ein {{< tooltip "Egress Port">}} beschreibt den Datenverkehr, der aus einem Switch herausfließt. Auf Deutsch: {{< termbase "Egress port">}}

<!-- {{% notice info %}}
The following examples refer to the following setup: All three streams that enter at three different ports of a switch are forwarded to the remaining port. The setup is shown in [Fig. 1](#fig-fqtss-routing).
{{% /notice %}} -->
{{% notice info %}}
Die folgenden Beispiele beziehen sich auf folgendes Szenario: Alle drei {{< termbase "Streams">}} gelangen über drei unterschiedliche {{< termbase "Ingress Ports">}} in den Switch und werden auf denselben {{< termbase "Egress Port">}} weitergeleitet. Der Aufbau wird in [Abb. 1](#fig-fqtss-routing) gezeigt. 
{{% /notice %}}

<!-- {{< figure src="/images/traffic-shaping-routing.drawio.svg" alt="Example Routing of 3 Streams" fig-num="1" title="Example Routing of 3 Streams" id="fig-fqtss-routing" >}} -->
{{< figure src="/images/traffic-shaping-routing.drawio.svg" alt="Routing von 3 Streams" fig-num="1" title="Routing von 3 Streams" id="fig-fqtss-routing" >}}

<!-- ## Strict Priority Forwarding -->
## Strict Priority Paket-Weiterleitung

<!-- The following figure shows all three streams from their respective {{< tooltip "ingress port" "Ingress port">}} forwarded to the {{< tooltip "egress port" "Egress port">}} considering Strict Priority Scheduling only. The packets are forwarded according to their priority immediately.  -->
Die Grafik in [Abb. 2](#fig-strict-prio) zeigt, wie alle drei {{< termbase "Streams">}} von ihren jeweiligen {{< termbase "Ingress Ports">}} zum {{< termbase "Egress Port">}} weitergeleitet werden. Dabei erfolgt die Weiterleitung nach dem Strict-Priority-Scheduling-Prinzip, also sofort entsprechend der Priorität der {{< termbase "Packets">}}:

<!-- - AV packets: packets have a high priority.
- Best-Effort: packets have low priority. -->
- AV {{< termbase "Packets">}}: haben hohe Priorität  
- Best-Effort (BE) {{< termbase "Packets">}}: haben niedrige Priorität

<!-- Considering strict priority forwarding only leads to time-critical packets being forwarded always first when the forwarding algorithm would have the choice between a time-critical and a Best-Effort packet. -->
Beim Strict-Priority-Forwarding werden {{< termbase "Packets">}}, die {{< termbase "time critical">}} sind, immer zuerst weitergeleitet, sobald eine Entscheidung zwischen {{< termbase "time critical">}} und {{< termbase "Best Effort">}} erforderlich ist.

<!-- This results in a blocking delay on lower-priority packets whenever high-priority packets are prioritized. -->
Dadurch kommt es bei niedrig priorisierten Paketen zu Verzögerungen, solange höher priorisierte {{< termbase "Packets">}} bevorzugt weitergeleitet werden.

<!-- Due to the fact, that without traffic shaping, packets that ingress the switch almost simultaneously will be forwarded immediately, the combined resulting stream will have a bursty temporal structure. -->
Ohne {{< termbase "Traffic Shaping">}} werden Pakete am {{< termbase "Ingress Port">}} nahezu sofort weitergeleitet. Dadurch entsteht am {{< termbase "Egress Port">}} ein schwankender Datenstrom.

<!-- {{< figure src="/images/traffic-shaping-strict-prio.drawio.svg" alt="Strict priority packet forwarding" fig-num="2" title="Strict Priority Packet Forwarding" id="fig-strict-prio" >}} -->
{{< figure src="/images/traffic-shaping-strict-prio.drawio.svg" alt="Strict priority Paket-Weiterleitung" fig-num="2" title="Strict Priority Paket-Weiterleitung" id="fig-strict-prio" >}}

<!-- ## Credit-based Forwarding -->
## Credit-based Paket-Weiterleitung

<!-- Using the Credit-based Shaper additionally to Strict Priority Scheduling as shown in [Fig. 2](#fig-strict-prio), can on one hand shape the resulting traffic stream into a uniformly distributed stream and on the other hand increase fairness towards lower priority traffic. -->
Durch den Einsatz eines Shapers (Deutsch: formt den Datenverkehr), der {{< termbase "credit based">}} ist, kann sich zusammen mit der Strict-Priority-Weiterleitung, wie in [Abb. 3](#fig-credit-based) gezeigt, ein Vorteil ergeben: Die {{< termbase "Packets">}} am {{< termbase "Egress Port">}} werden gleichmäßiger verteilt, und die Fairness gegenüber niedrig priorisierten Paketen wird erhöht.


<!-- The core idea behind the Credit-based Shaper is simple:   -->
Die grundlegende Idee des {{< termbase "credit based" >}}en Shapers ist einfach:

<!-- Each priority level has a credit counter.   -->
Jeder Prioritätsklasse wird ein {{< termbase "Credit Counter">}} zugewiesen.

<!-- - It decreases when packets are being transmitted.  
- This counter builds up when packets are waiting to be sent.   -->
- Der {{< termbase "Credit Counter">}} verringert sich, während {{< termbase "Packets">}} übertragen werden.  
- Der {{< termbase "Credit Counter">}} steigt an, solange {{< termbase "Packets">}} auf die Übertragung warten.

<!-- As soon as there is an opportunity to send data and the credit for a particular priority level is above zero, packets of that priority can be transmitted. -->
Sobald der {{< termbase "Credit Counter">}} größer als Null ist und der {{< termbase "Egress Port">}} frei ist, können Pakete dieser Prioritätsklasse übertragen werden.

<!-- This approach spreads packet transmissions more evenly over time, reducing burstiness and smoothing traffic flow. Simultaneously lower priority traffic has the opportunity to be forwarded in the resulting gaps, when higher priority packet transmission is temporally not allowed due to a credit value lower than 0. In practice, the rate at which credit decreases (*sendSlope*) and increases (*idleSlope*) is calculated based on the amount of bandwidth that is reserved. -->
Dieser Ansatz verteilt die {{< termbase "Packets">}} gleichmäßiger über die Zeit und reduziert Spitzen im Datenverkehr. Gleichzeitig können Pakete niedrigerer Priorität in den Lücken weitergeleitet werden, wenn der {{< termbase "Credit Counter">}} der höher priorisierten Klasse unter Null liegt. In der Praxis werden die Raten, mit denen der {{< termbase "Credit Counter">}} abnimmt (*sendSlope*) bzw. zunimmt (*idleSlope*), anhand der reservierten Bandbreite berechnet.

<!-- {{< figure src="/images/traffic-shaping-qav.drawio.svg" alt="Credit-based packet forwarding" fig-num="3" title="Credit-Based Packet Forwarding" id="fig-credit-based">}} -->
{{< figure src="/images/traffic-shaping-qav.drawio.svg" alt="Credit-based Paket-Weiterleitung" fig-num="3" title="Credit-Based Paket-Weiterleitung" id="fig-credit-based">}}
