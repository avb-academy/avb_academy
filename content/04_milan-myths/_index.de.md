---
title: "Milan Mythen"
date: 2025-08-04
weight: 3
---

<!-- There are several persistent myths surrounding Milan and its foundational technology, AVB. -->
<!-- This page addresses the most common misconceptions with clear, technically accurate explanations. -->
Es gibt einige hartnäckige Mythen über das Milan-Protokoll und die zugrunde liegende AVB-Technologie.  
Auf dieser Seite werden die häufigsten Missverständnisse erläutert und die tatsächliche Sachlage verständlich erklärt.

## Inhaltverzeichnis
<!-- - [Myth: AVB is obsolete](#myth-avb-is-obsolete)
- [Myth: Milan is proprietary](#myth-milan-is-proprietary)
- [Myth: Milan is old and outdated](#myth-milan-is-old-and-outdated)
- [Myth: Milan always has a latency of 2ms](#myth-milan-always-has-a-latency-of-2ms)
- [Myth: There are no AVB-capable switches available](#myth-there-are-no-avb-capable-switches-available)
- [Myth: Milan always blocks 75% of the available network bandwidth](#myth-milan-blocks-75-of-the-available-network-bandwidth)
- [Myth: Milan control is still under development](#myth-milan-control-is-still-under-development) -->
- [Mythos: AVB ist veraltet](#myth-avb-is-obsolete)
- [Mythos: Milan ist nicht mehr zeitgemäß](#myth-milan-is-old-and-outdated)
- [Mythos: Milan Bei Milan handelt es sich um ein proprietäres Protokoll](#myth-milan-is-proprietary)
- [Mythos: Milan hat immer eine Latenz von 2 ms](#myth-milan-always-has-a-latency-of-2ms)
- [Mythos: Es gibt kaum Switches, die AVB unterstützen](#myth-there-are-no-avb-capable-switches-available)
- [Mythos: Milan blockiert immer 75 % der verfügbaren Netzwerk-Bandbreite](#myth-milan-blocks-75-of-the-available-network-bandwidth)
- [Mythos: Das Milan-Steuerprotokoll wird immer noch entwickelt](#myth-milan-control-is-still-under-development)

<!-- {{% notice info %}}  
This page assumes you are familiar with the relationship between AVB and Milan.  
For a brief overview, see the [AVB Academy introduction](../_index.md).  
{{% /notice %}} -->

{{% notice info %}}
Die Informationen auf dieser Seite setzen voraus, dass du mit den Grundlagen von AVB und Milan vertraut bist.  
Für eine kurze Übersicht kannst du die [AVB Academy Einleitung](../_index.md) lesen.
{{% /notice %}}

---

<a id="myth-avb-is-obsolete"></a>
<!-- {{% notice style="warning" title="Myth: AVB is obsolete" icon="fa-solid fa-circle-question"%}}
It is often claimed that AVB is obsolete because the IEEE AVB working group ended its activities in 2012 when it was renamed into the Time-Sensitive Networking (TSN) task group to focus on industrial applications.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: AVB ist veraltet" icon="fa-solid fa-circle-question"%}}
Häufig wird behauptet, AVB sei veraltet. Grund dafür sei, dass die IEEE AVB-Arbeitsgruppe 2012 ihre Aktivitäten eingestellt habe. Sie wurde in die Time-Sensitive Networking (TSN) Task Group umbenannt, um den Fokus stärker auf industrielle Anwendungen zu legen.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: AVB is very much alive" icon="fa-solid fa-circle-check"%}}
The AVB specification (IEEE 802.1BA) is still active and maintained, with the latest revision published in 2021. The renaming of the working group reflected an expanded scope, not a move away from AVB.

Audio and video transport remains a core use case within TSN, alongside newer applications in industrial automation, automotive, and aerospace. Rather than being obsolete, AVB has evolved within a broader standards family.
{{% /notice %}} -->
{{% notice style="tip" title="Realität: AVB ist nach wie vor aktiv" icon="fa-solid fa-circle-check"%}}
Die AVB-Spezifikation (IEEE 802.1BA) ist weiterhin aktiv und wird stetig gepflegt; die aktuellste Veröffentlichung stammt aus dem Jahr 2021. Die Umbenennung der Arbeitsgruppe spiegelt lediglich eine Erweiterung ihres Aufgabenbereichs wider, nicht das Ende von AVB.

Die Übertragung von Audio- und Videodaten bleibt ein zentraler Anwendungsbereich innerhalb von TSN. Gleichzeitig gibt es neue Einsatzgebiete wie die Industrieautomatisierung, der Automotive-Bereich und in der Luft- und Raumfahrt. AVB ist also keineswegs veraltet, sondern hat sich innerhalb einer größeren Standardfamilie weiterentwickelt.
{{% /notice %}}

---

<a id="myth-milan-is-old-and-outdated"></a>
<!-- {{% notice style="warning" title="Myth: Milan is old and outdated" icon="fa-solid fa-circle-question"%}}
Milan is sometimes perceived as a legacy solution that has been surpassed by newer, IP-based audio networking technologies.

See also: [Myth: AVB is obsolete](#myth-avb-is-obsolete)
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Milan ist nicht mehr zeitgemäß" icon="fa-solid fa-circle-question"%}}
Milan wird manchmal als veraltete Technologie wahrgenommen. Kritiker meinen, es sei von neueren, IP-basierten Audio-Netzwerken überholt worden.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Milan is one of the most modern audio networking standards" icon="fa-solid fa-circle-check"%}}
Milan is actually among the most recent professional audio networking standards. It was first released in 2018, while widely adopted IP-based standards like AES67 date back to 2013.

More importantly, Milan provides deterministic performance and precise timing that IP-based solutions still struggle to match. It combines Ethernet transport with guaranteed delivery and bounded latency, making it ideal for high-performance audio applications.
{{% /notice %}} -->
{{% notice style="tip" title="Realität: Milan ist einer der modernsten Audio-Netzwerk-Standards" icon="fa-solid fa-circle-check"%}}
Tatsächlich ist Milan einer der neuesten professionellen Audio-Netzwerk-Standards. Die erste Version wurde 2018 veröffentlicht. Zum Vergleich: Weit verbreitete IP-basierte Standards wie AES67 stammen bereits aus dem Jahr 2013.

Wichtiger noch: Milan liefert deterministische Performance und präzises Timing, das IP-basierte Lösungen oft nur schwer erreichen. Es kombiniert Ethernet-Transport mit garantierter Zustellung und begrenzter Latenz, was es ideal für Anwendungen mit hoher Audio-Performance macht.
{{% /notice %}}

---

<a id="myth-milan-is-proprietary"></a>
<!-- {{% notice style="warning" title="Myth: Milan is a proprietary protocol" icon="fa-solid fa-circle-question"%}}
Some claim that Milan is a proprietary protocol, used exclusively by a selected group of ProAV manufacturers.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Bei Milan handelt es sich um ein proprietäres Protokoll" icon="fa-solid fa-circle-question"%}}
Es wird behauptet, dass Milan ein proprietäres Protokoll sei. Demnach könne es nur von einer ausgewählten Gruppe von ProAV-Herstellern genutzt werden.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Milan is based on open IEEE standards" icon="fa-solid fa-circle-check"%}}
Milan is not proprietary. It is a clearly defined, open specification built on top of IEEE open standards including 802.1AS (time synchronization), 802.1Q (traffic shaping), 1722 (streaming transport), and 1722.1 (device discovery and control).

The Milan protocol is developed collaboratively by leading ProAV manufacturers within the Avnu Alliance, ensuring it meets the real-world needs of professional users. Any manufacturer can implement Milan without licensing fees, and the full specification is freely available from the [Avnu Alliance website](https://avnu.org/resource/milan-specification/).
{{% /notice %}} -->
{{% notice style="tip" title="Realität: Milan basiert auf offenen IEEE-Standards" icon="fa-solid fa-circle-check"%}}
Milan ist nicht proprietär. Es handelt sich um eine offene Spezifikation, die auf IEEE-Standards aufbaut, darunter 802.1AS (Zeitsynchronisation), 802.1Q (Traffic Shaping), 1722 (Streaming Transport) und 1722.1 (Geräteerkennung und -steuerung).

Das Milan-Protokoll wird von führenden ProAV-Herstellern innerhalb der Avnu Alliance gemeinsam entwickelt. So wird sichergestellt, dass es den Anforderungen professioneller Anwender entspricht. Jeder Hersteller kann Milan implementieren, ohne Lizenzgebühren zu zahlen. Die vollständige Spezifikation ist kostenlos auf der [Avnu Alliance Website](https://avnu.org/resource/milan-specification/) verfügbar.
{{% /notice %}}

---

<a id="myth-milan-always-has-a-latency-of-2ms"></a>
<!-- {{% notice style="warning" title="Myth: Milan always has a latency of 2ms" icon="fa-solid fa-circle-question"%}}
Because AVB networks originally introduced a default latency of 2ms, some believe this is the fixed or only possible latency for Milan systems.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Milan hat immer eine Latenz von 2 ms" icon="fa-solid fa-circle-question"%}}
Manche glauben, dass Milan immer eine Latenz von 2ms hat. Hintergrund ist der Standardwert für AVB-Netzwerke, der bei 2ms liegt. Daraus entsteht die Annahme, dass dieser Wert unveränderlich sei und die einzige mögliche Einstellung für Milan darstellen würde.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Milan guarantees a bounded latency, not a fixed one" icon="fa-solid fa-circle-check"%}}
Milan networks are fully time-aware. All devices, including switches, share a synchronized understanding of time. This enables them to calculate and guarantee precise end-to-end transmission delays.

As a result, Milan can guarantee a minimum playout delay tailored to the specific path and stream characteristics. Typical configurations range from 0.25 ms to 2 ms.
{{% /notice %}} -->
{{% notice style="tip" title="Realität: Milan garantiert eine begrenzte, aber nicht feste Latenz" icon="fa-solid fa-circle-check"%}}
Milan-Netzwerke sind vollständig time-aware. Alle Geräte im Netzwerk, einschließlich der Switches, haben die gleiche absolute Zeit. Dadurch lassen sich die Ende-zu-Ende-Übertragungszeiten präzise berechnen und garantieren.

Milan kann eine minimale Ausspielverzögerung bereitstellen, die auf dem Netzwerkpfad und den Eigenschaften des Audio-Streams basiert. Typische Werte liegen zwischen 0,25ms und 2ms.
{{% /notice %}}

---

<a id="myth-there-are-no-avb-capable-switches-available"></a>
<!-- {{% notice style="warning" title="Myth: There are no AVB-capable switches available" icon="fa-solid fa-circle-question"%}}
It is often claimed that Milan is impractical because it requires specialized switches, and that mainstream networking vendors no longer support AVB.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Es gibt kaum Switches, die AVB unterstützen" icon="fa-solid fa-circle-question"%}}
Es gibt Behauptungen, dass Milan unpraktisch sei. Hintergrund ist, dass spezielle Switches benötigt werden und dass große Hersteller AVB nicht mehr unterstützen würden.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Certified AVB switches are widely available" icon="fa-solid fa-circle-check"%}}
AVB-capable switches incorporate advanced Ethernet technologies such as the Precision Time Protocol v2 (PTPv2) for precise clock synchronization. Additionally, they implement traffic shaping and bandwidth reservation mechanisms defined by the AVB standards to guarantee bounded latency and deterministic delivery of audio streams.

A wide range of manufacturers produce certified AVB switches, including Netgear, Cisco, Extreme Networks, Luminex, Niveo Professional, Adamson Systems Engineering, d&b audiotechnik, L-Acoustics, and others. The ecosystem continues to expand with new certified products regularly introduced.

You can find the current list of certified switches in the Avnu Alliance [Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Network%20Device).
{{% /notice %}} -->
{{% notice style="tip" title="Realität: AVB-zertifizierte Switches sind weit verbreitet" icon="fa-solid fa-circle-check"%}}
AVB-fähige Switches nutzen neueste Ethernet-Technologien wie das Precision Time Protocol v2 (PTPv2) für die präzise Zeitsynchronisation. Außerdem setzen sie Mechanismen für Traffic Shaping und Bandbreitenmanagement um, wie es die AVB-Spezifikation verlangt. So wird eine garantierte obere Grenze für die Übertragungszeit erreicht und Audio-Streams werden deterministisch übertragen.

Eine große Anzahl an Herstellern stellt zertifizierte AVB-Switches her. Unter den Herstellern sind Firmen wie Netgear, Cisco, Extreme Networks, Luminex, Niveo Professional, Adamson Systems Engineering, d&b audiotechnik, L-Acoustics und viele andere. Die Liste wird stetig erweitert.  

Die aktuelle Übersicht aller AVB-zertifizierten Switches der Avnu Alliance ist auf der [Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Network%20Device) verfügbar.
{{% /notice %}}

---

<a id="myth-milan-blocks-75-of-the-available-network-bandwidth"></a>
<!-- {{% notice style="warning" title="Myth: Milan always blocks 75% of the available network bandwidth" icon="fa-solid fa-circle-question"%}}
There is a persistent belief that Milan blocks 75% of the network bandwidth, severely limiting other traffic.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Milan blockiert immer 75 % der verfügbaren Netzwerk-Bandbreite" icon="fa-solid fa-circle-question"%}}
Es hält sich der hartnäckige Glaube, dass Milan immer 75 % der verfügbaren Netzwerk-Bandbreite reserviert. Demnach würde anderer Netzwerkverkehr stark eingeschränkt werden.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Your network is not 75% full by default" icon="fa-solid fa-circle-check"%}}
Milan uses bandwidth reservation to guarantee time-sensitive delivery, but only reserves the bandwidth required by each stream. For example, an 8-channel stream at 48 kHz reserves around 17 Mbps.

All remaining bandwidth is available for other traffic. The 75% figure refers to the maximum possible reservation (based on AVB Class A and B limits), not the typical usage. You can find a detailed calculation in the description of the [Stream Reservation Protocol](../01_milan/03_traffic-shaping/stream-reservation/_index.md).
{{% /notice %}} -->
{{% notice style="tip" title="Realität: Dein Netzwerk ist nicht zu 75 % blockiert" icon="fa-solid fa-circle-check"%}}
Milan nutzt Bandbreiten-Reservierung, um zeitkritische Daten zuverlässig zu übertragen. Es wird jedoch nur so viel Bandbreite reserviert, wie für jeden Stream nötig ist. Zum Beispiel benötigt ein 8-Kanal-Stream bei 48 kHz etwa 17 Mbps.

Die restliche Bandbreite bleibt frei und kann für andere Anwendungen genutzt werden. Die Zahl 75 % beschreibt lediglich die maximale mögliche Reservierung (basierend auf den AVB Class A und Class B Grenzen). Eine detaillierte Berechnung für die Stream-Reservierung findest du hier: [Stream Reservation Protocol](../01_milan/03_traffic-shaping/stream-reservation/_index.md).
{{% /notice %}}

---

<a id="myth-milan-control-is-still-under-development"></a>
<!-- {{% notice style="warning" title="Myth: Milan control is still under development" icon="fa-solid fa-circle-question"%}}
It is sometimes assumed that Milan control is incomplete or still evolving, making it unsuitable for real-world deployment.
{{% /notice %}} -->
{{% notice style="warning" title="Mythos: Das Milan-Steuerprotokoll wird immer noch entwickelt" icon="fa-solid fa-circle-question"%}}
Es wird gelegentlich angenommen, dass das Milan-Steuerprotokoll noch unvollständig ist und sich weiterhin in Entwicklung befindet. Deshalb sei Milan für den praktischen Einsatz ungeeignet.
{{% /notice %}}

<!-- {{% notice style="tip" title="Reality: Milan control is fully defined and standardized" icon="fa-solid fa-circle-check"%}}
Milan uses the ATDECC protocol (defined in IEEE 1722.1) for control, which defines standardized mechanisms for device discovery, enumeration, and stream management.

These control capabilities have been part of the Milan specification since its initial release and are already implemented in certified Milan devices.
{{% /notice %}} -->
{{% notice style="tip" title="Realität: Das Milan-Steuerprotokoll ist vollständig entwickelt und standardisiert" icon="fa-solid fa-circle-check"%}}
Milan nutzt das ATDECC-Protokoll (definiert in IEEE 1722.1) für die Steuerung. Es legt standardisierte Mechanismen für Geräteerkennung, -enumeration und Stream-Management fest.

Diese Steuerfunktionen sind seit der ersten Milan-Spezifikation definiert und bereits in zertifizierten Milan-Geräten implementiert.
{{% /notice %}}
