---
title: "Switches"
date: 2025-02-11
weight: 40
---

<!-- {{% notice info %}}
- The Switches are not included in the Milan specification - only Endstations are. Therefore, Switches are AVB certified.
- Ingress port: Input port
- Egress port: Output port
{{% /notice %}} -->
{{% notice info %}}
- Switches werden in der Milan-Spezifikation nicht berücksichtigt – nur {{< termbase "Endstations">}}. Daher sind Switches AVB-zertifiziert.
- Ingress-Port: {{< termbase "Ingress Port">}}
- Egress-Port: {{< termbase "Egress Port">}}
{{% /notice %}}

<!-- AVB {{< tooltip "Switches" "Switch">}} do not require manual QoS configuration, as it is common with other Audio over IP protocols. With Milan, QoS configuration is automatically managed by the protocol. The fundamentals are detailed in [Stream Reservation Protocol (SRP)](../01_milan/03_traffic-shaping/stream-reservation/_index.md). -->
AVB {{< tooltip "Switches" "Switch">}} benötigen keine manuelle Konfiguration der QoS-Parameter, wie es bei anderen Audio-over-IP-Protokollen üblich ist. Das Milan-Protokoll verfügt über Mechanismen, die die Konfiguration automatisch übernehmen. Die Grundlagen der Stream-Reservierung werden im [Stream-Reservierung-Protokoll (SRP)](../01_milan/03_traffic-shaping/stream-reservation/_index.md) erläutert.

<!-- As mentioned in [Network Synchronization](../01_milan/00_network-timing/_index.md), one of the key advantages of a Milan network is that all participants share a common understanding of network time. This enables a fully deterministic transmission chain from the {{< tooltip "Talker" >}} to the {{< tooltip "Listener" >}}, allowing precise evaluation of whether a {{< tooltip "Delay">}} deadline can be met before the packet is sent. Unlike other audio network protocols on the market, Milan is the only one that guarantees full determinism, ensuring predictable and reliable audio transmission in all scenarios. -->
Wie bereits im Kapitel [Netzwerksynchronisation](../01_milan/00_network-timing/_index.md) erwähnt, ist einer der Hauptvorteile eines Milan-Netzwerks, dass alle Teilnehmer ein gemeinsames Verständnis der Netzwerkzeit haben. Dies ermöglicht eine vollständig deterministische Übertragungskette vom {{< tooltip "Talker">}} zum {{< tooltip "Listener">}}, wodurch genau vorhergesagt werden kann, ob eine {{< tooltip "Delay">}}-Deadline eingehalten wird – sogar bevor das Paket gesendet wird. Im Gegensatz zu anderen Audio-Netzwerkprotokollen auf dem Markt ist Milan das einzige Protokoll, das eine vollständig deterministische Übertragung garantiert und damit eine vorhersehbare und zuverlässige Audioübertragung in allen Szenarien sicherstellt.

<!-- The AVB certification process ensures that all relevant features are supported by a switch. Therefore, only AVB-certified {{< tooltip "Switches" "Switch">}} are recommended for use in a Milan AVB network. A list of certified {{< tooltip "Switches" "Switch">}} is available on the Avnu website: [Certified Product Registry](https://avnu.org/certified-product-registry?cert=Network%20Device&type=). -->
Der AVB-Zertifizierungsprozess stellt sicher, dass alle für Milan relevanten Funktionen von einem Switch unterstützt werden. Daher werden nur AVB-zertifizierte {{< tooltip "Switches" "Switch">}} für den Einsatz in einem Milan-AVB-Netzwerk empfohlen. Eine Liste aller zertifizierten Produkte ist auf der Avnu-Website verfügbar: [Certified Product Registry](https://avnu.org/certified-product-registry?cert=Network%20Device&type=).

<!-- When digging deeper in the functionality of a switch, it is important to understand that ports are defined based on the direction of the data flow under investigation: an ingress port serves as the input (mnemonic: ingress = input), while an egress port serves as the exit (mnemonic: egress = exit). For example, the traffic shaping mechanisms described in [Forward Queuing for Time-Sensitive Streams (FQTSS)](../01_milan/03_traffic-shaping/fqtss/_index.md) refer to the {{< tooltip "egress" "Egress port">}} port of a switch. -->
Beim genaueren Betrachten der Funktionalität eines Switches ist es wichtig, die Richtung des Datenflusses zu verstehen. Daher wird zwischen {{< termbase "Ingress Port">}} und {{< termbase "Egress Port">}} unterschieden. Zum Beispiel beziehen sich die im Kapitel [Forward Queuing for Time-Sensitive Streams (FQTSS)](../01_milan/03_traffic-shaping/fqtss/_index.md) beschriebenen Traffic-Shaping-Mechanismen auf den {{< termbase "Egress Port">}} eines Switches.
