---
title: "Datenübertragung"
date: 2025-02-11
weight: 2
---

<!-- {{% notice info %}}
- Data is encapsulated in Streams to use available bandwidth more efficiently.
- Audio transport in Milan: 32bit PCM data.
- Media Time controls playback/recording in relation to the Network Time.
- A Stream has a configurable Presentation Time Offset in the range of 0.25ms to 2ms.
- Bandwidth usage of Streams is explained in the [Traffic Shaping](../03_traffic-shaping/stream-reservation/_index.md#how-much-traffic-is-reserved-for-my-audio-stream) section.
{{% /notice %}} -->
{{% notice info %}}
- Daten werden in {{< termbase "Streams">}} gebündelt, um die verfügbare {{< termbase "Bandwidth">}} effizient zu nutzen.  
- Der {{< termbase "Media Time">}} steuert {{< termbase "Playback">}} und {{< termbase "Recording">}} im Verhältnis zur {{< termbase "Network Time">}}.  
- Ein {{< termbase "Stream">}} hat eine einstellbare {{< termbase "Presentation Time Offset">}} im Bereich von 0,25 ms bis 2 ms.  
- Die {{< termbase "Bandwidth Usage">}} von {{< termbase "Streams">}} wird im Kapitel [Traffic Shaping](../03_traffic-shaping/stream-reservation/_index.md) erläutert.  
{{% /notice %}}

<!-- ## Audio Data -->
## Audiodaten

<!-- In Milan AVB, audio data is transmitted via {{< tooltip "Streams" "Stream">}} using the Audio Video Transmission Protocol (AVTP), which defines the structure of the data frames sent across the network. -->
In {{< termbase "Milan">}} {{< termbase "AVB">}} werden Audiodaten über {{< tooltip "Streams" "Stream">}} übertragen. Grundlage dafür ist das Audio Video Transmission Protocol (AVTP), das die Struktur der zu übertragenden {{< termbase "Packets">}} definiert.

<!-- The specification adopts the AVTP Audio Format (AAF) for audio transport. This is not to be confused with the Advanced Authoring Format. It mandates that each {{< tooltip "PCM">}} sample be transmitted as a 32-bit value, with shorter samples zero-padded as needed. -->
Die {{< termbase "Specification">}} verwendet das AVTP Audio Format (AAF) für die Übertragung von Audiodaten. Hinweis: Dabei handelt es sich nicht um das Advanced Authoring Format.  
Die {{< tooltip "AAF">}}-Spezifikation legt fest, dass jedes {{< tooltip "PCM">}}-Sample als 32-Bit-Wert übertragen wird. Kürzere Samples werden mit Nullen aufgefüllt, um die Wortbreite zu erreichen.

<!-- A {{< tooltip "Talker">}} in a Milan network defines the outgoing {{< tooltip "Stream">}} format, specifying the number of audio channels in the {{< tooltip "Stream">}}. The {{< tooltip "Listener">}} is required to adapt to the format provided by the {{< tooltip "Talker">}}. -->
Im {{< termbase "Milan">}}-Netzwerk legt der {{< tooltip "Talker">}} das Format des {{< tooltip "Streams" "Stream">}} fest. Dabei bestimmt er die {{< termbase "Sample Rate">}} sowie die Anzahl der Audiokanäle pro {{< termbase "Stream">}}.  
Der {{< tooltip "Listener">}} passt sich automatisch an das vom {{< tooltip "Talker">}} bereitgestellte Format an.

<!-- The Milan Base Format specifies support for channel counts of either 1, 2, 4, 6, 8 audio channels per {{< tooltip "Stream">}}. The support for the Base Format is mandatory for {{< tooltip "Listeners" "Listener">}} and part of the Milan [certification](../../02_user-guides/certified-products.md). This ensures interoperability between any {{< tooltip "Talker">}} and {{< tooltip "Listener">}}. -->
Das {{< termbase "Milan">}} Base Format unterstützt Konfigurationen mit entweder 1, 2, 4, 6 oder 8 Audiokanäle pro {{< termbase "Stream">}} sowie {{< termbase "Sample Rates">}} von 48 kHz, 96 kHz und 192 kHz.  
Jeder {{< tooltip "Listener">}} muss das Base Format unterstützen; dies wird im Rahmen der {{< termbase "Milan">}} [Zertifizierung](../../02_user-guides/certified-products.md) überprüft.  
So wird die {{< termbase "Interoperability">}} zwischen {{< tooltip "Talker">}} und {{< tooltip "Listener">}} gewährleistet.

<!-- <div class="text-image-container">
  <div class="text">
    <p>A {{< tooltip "Stream">}} can be viewed as a container for audio data. In addition to the audio content, it also includes Ethernet information, such as the source and destination {{< tooltip "MAC">}} addresses. Ethernet information is present in every packet. This mandatory overhead for each packet should make it evident that using a larger number of audio channels per {{< tooltip "Stream">}} is more efficient than using a smaller number.</p>
  </div>
  <div class="image">
    <img src="/images/stream-format.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div> -->
<div class="text-image-container">
  <div class="text">
    <p>Ein {{< termbase "Stream">}} kann als Container für Audiodaten betrachtet werden. Neben den Audiosamples enthält der Stream auch Ethernet-Informationen wie die Quell- und Ziel-{{< tooltip "MAC">}}-Adresse. Diese Informationen sind in jedem Ethernet-Paket enthalten.  
    Dieser unvermeidbare Overhead macht deutlich, dass die Übertragung einer größeren Anzahl von Audiokanälen pro Stream effizienter ist als die Nutzung vieler kleiner Streams.</p>
  </div>
  <div class="image">
    <img src="/images/stream-format.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

<!-- It is worth noting that a {{< tooltip "Stream">}} is configured with a fixed {{< tooltip "PTO" >}} before it starts streaming. The value range for the PTO is from 0.25ms to 2ms. Due to the fact that all devices in the network have a shared understanding of time, it is possible with Milan to guarantee the latency that has been configured for the {{< tooltip "Stream">}}. Details on how this is possible are described in [Traffic Shaping Section](../03_traffic-shaping/_index.md). -->
Ein {{< termbase "Stream">}} wird mit einer festen {{< tooltip "PTO">}} konfiguriert, bevor die Übertragung beginnt. Der Wertebereich der {{< termbase "Presentation Time Offset">}} liegt zwischen 0,25 ms und 2 ms.  
Da alle Geräte im Netzwerk ein gemeinsames Verständnis von Zeit besitzen, kann {{< termbase "Milan">}} die konfigurierte {{< tooltip "PTO">}} eines Streams garantieren.  
Weitere Informationen dazu finden sich im Kapitel [{{< termbase "Traffic Shaping">}}](../03_traffic-shaping/_index.md).

<!-- ## Media Clock Data -->
## {{< termbase "Media Time">}} Daten {#media-time-daten}

<!-- The previous section [Network Synchronization](../00_network-timing/_index.md) explains the distinction between {{< tooltip "Network Time">}} and {{< tooltip "Media Time">}} in {{< tooltip "Milan">}}. -->
Im vorherigen Kapitel [Netzwerksynchronisation](../00_network-timing/_index.md) wurde der Unterschied zwischen {{< termbase "Network Time">}} und {{< termbase "Media Time">}} in {{< termbase "Milan">}} erläutert.

<!-- In summary: -->
Zusammengefasst lässt sich sagen:
<!-- - **Network Time** is the shared global time base provided to all devices in the network by {{< tooltip "gPTP">}}. -->
<!-- - **Media Time** is the timing domain used specifically to synchronize audio recording and playback clocks in Endstations. -->
- Die **{{< termbase "Network Time">}}** beschreibt die globale Zeitbasis, die von allen Geräten im Netzwerk über {{< tooltip "gPTP">}} gemeinsam genutzt wird.  
- Der **{{< termbase "Media Time">}}** bezeichnet die Zeitdomäne, die zur Synchronisation der Audio-{{< termbase "Recording">}}- und {{< termbase "Playback">}}-Takte in den {{< termbase "Endstation">}}en verwendet wird.

<!-- From a transport perspective, a {{< tooltip "Stream">}} can carry either audio data or Media Time clocking data. -->
Aus Sicht der {{< termbase "Media Transport">}} kann ein {{< termbase "Stream">}} entweder Audiodaten oder den {{< termbase "Media Time">}} übertragen.
