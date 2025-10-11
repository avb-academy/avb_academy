---
title: "Netzwerksynchronisation"
date: 2025-02-11
weight: 1
---
<!-- 
{{% notice info %}}
- A Milan AVB network has one clock leader. The BTCA is executed automatically each time a change in the network occurs to elect a GrandMaster (GM).
- The GM is elected based on parameters that describe the clock quality of the device. The best quality wins.
- Network Time is the shared global time base provided to all devices in the network by gPTP.
- Media Time is the timing domain used specifically to synchronize audio recording and playback clocks in Endstations.
{{% /notice %}} -->
{{% notice info %}}
- Ein Milan AVB Netzwerk hat einen {{< termbase "Clock Leader" >}}. Der BTCA wird automatisch ausgeführt, sobald sich etwas im Netzwerk ändert, und wählt dabei den besten {{< termbase "Grandmaster" >}} aus.  
- Der GM wird auf Grundlage von Parametern bestimmt, die die {{< termbase "Clock" >}} Qualität des Geräts beschreiben. Die höchste Qualität gewinnt.  
- Die {{< termbase "Network Time" >}} ist die gemeinsame {{< termbase "Time Base" >}}, die allen Geräten im {{< termbase "Network" >}} durch gPTP bereitgestellt wird.  
- Die {{< termbase "Media Time" >}} bezeichnet die Zeitdomäne, die speziell genutzt wird, um die {{< termbase "Recording" >}}- und {{< termbase "Playback" >}}-{{< termbase "Clock" >}}s in Endstations zu synchronisieren.  
{{% /notice %}}

<!-- Having a well-synchronized network is crucial for the performance of the network. An unsynchronized network could lead to sampling signals at different points in time. In a less severe scenario, this can result in mixed signals that exhibit a comb filter characteristic, distorting the audio. In a worst-case scenario, the lack of synchronization could cause audio dropouts, glitches, and clicks, significantly degrading the listening experience. Therefore, maintaining precise synchronization is essential to ensure seamless and high-quality audio transmission across the network. -->
Ein präzise synchronisiertes {{< termbase "Network" >}} ist entscheidend für die {{< termbase "Network Performance" >}}. In einem unsynchronisierten Netzwerk könnten {{< termbase "Audio Stream" >}}s zu unterschiedlichen Zeitpunkten {{< termbase "Sampling" >}} werden.  
In einem weniger schlimmen Szenario kann dies zu {{< termbase "Comb Filter" >}}-Effekten führen und die Audioqualität beeinträchtigen.  
Im schlimmsten Fall kann die fehlende {{< termbase "Synchronization" >}} {{< termbase "Audio Dropout" >}}, {{< termbase "Glitch" >}}s und {{< termbase "Click" >}}-Geräusche verursachen, was die Hörerfahrung erheblich verschlechtert.  
Daher ist eine präzise {{< termbase "Synchronization" >}} unerlässlich, um eine nahtlose und hochwertige Audioübertragung im {{< termbase "Network" >}} sicherzustellen.

<!-- Milan AVB employs the Generalized Precision Timing Protocol (gPTP) to synchronize all participants within the network, including both Endstations and switches. Notably, the inclusion of Switches distinguishes Milan from other existing networked audio protocols, as it requires the Switches to be time-aware and therefore capable of understanding Network time. -->
Milan AVB benutzt das Generalized Precision Timing Protocol (gPTP), um alle Teilnehmer im {{< termbase "Network" >}} zu synchronisieren, einschließlich der {{< tooltip "Endstations" "Endstation" >}} und der {{< tooltip "Switches" "Switch" >}}.  
Auffallend ist, dass Milan sich durch die {{< termbase "Synchronization" >}} der Switches von anderen {{< termbase "Networked Audio" >}}-Protokollen unterscheidet. Damit die Synchronisation funktioniert, müssen die Switches {{< termbase "Time Aware" >}} sein und die {{< termbase "Network Time" >}} korrekt verarbeiten können.

<!-- Milan timing is divided into two parts: the {{< tooltip "Network Time">}}, provided to all participants of the network via {{< tooltip "gPTP" >}}, and the timing information that controls the audio sampling clock, referred to as {{< tooltip "Media Time">}}. To avoid confusion between the two domains, these terms clearly distinguish global synchronization from audio-specific clock control. -->
Das Timing in Milan ist in zwei Bereiche unterteilt:  
- Die {{< termbase "Network Time" >}}, die allen Teilnehmern des {{< termbase "Network" >}} über {{< tooltip "gPTP">}} bereitgestellt wird.  
- Der {{< termbase "Media Time" >}}, die die Audio-{{< termbase "Sampling" >}}-{{< termbase "Clock" >}} steuert.  

Damit lässt sich klar zwischen der globalen {{< termbase "Synchronization" >}} im Netzwerk und der audio-spezifischen Taktung unterscheiden.

<!-- ## Network Clock Leader Election -->
## Auswahl des {{< termbase "Clock Leader" >}} im {{< termbase "Network" >}}

<!-- <div class="text-image-container">
  <div class="text">
    <p>Consider a Milan network that has just been switched on. It is likely that it consists of multiple {{< tooltip "Endstations">}} and {{< tooltip "Switches" "Switch">}}. In a first step, a Grand Master (GM) has to be elected. This Grand Master will distribute its time to all participants allowing them to share a common understanding of time. The election process is defined in an algorithm called Best Time Transmitter Algorithm (BTCA). The algorithm is executed automatically when a change in the network is detected.</p>
  </div>
  <div class="image">
    <img src="/images/gPTP-BTCA.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div> -->
<div class="text-image-container">
  <div class="text">
    <p>Betrachten wir ein Milan {{< termbase "Network" >}}, das gerade eingeschaltet wurde. Es besteht vermutlich aus mehreren {{< tooltip "Endstations" "Endstation" >}} und {{< tooltip "Switches" "Switch" >}}.  
    Im ersten Schritt muss ein {{< termbase "Grandmaster" >}} (GM) gewählt werden. Dieser verteilt seine {{< termbase "Network Time" >}} an alle Teilnehmer, sodass alle Geräte eine gemeinsame Zeitbasis haben.  
    Der Auswahlprozess wird durch den Best Time Transmitter Algorithm (BTCA) definiert und läuft automatisch ab, sobald eine Änderung im {{< termbase "Network" >}} erkannt wird.
    </p>
  </div>
  <div class="image">
    <img src="/images/gPTP-BTCA.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

<!-- The election of the {{< tooltip "gPTP" >}} GrandMaster is based on parameters that describe the clock quality of the device. Of course the best clock quality is elected as the {{< tooltip "GM">}}. In case multiple devices have the same clock quality, the device with the lowest {{< tooltip "MAC" >}} address is selected. Switches are preferred over Endstations. -->
Die Wahl des {{< tooltip "gPTP" >}} {{< termbase "Grandmaster" >}} basiert auf Parametern, die die {{< termbase "Clock" >}}-Qualität des Geräts beschreiben.  
Das Gerät mit der höchsten {{< termbase "Clock" >}}-Qualität wird als {{< termbase "Grandmaster" >}} ausgewählt.  
Besitzen mehrere Geräte die gleiche {{< termbase "Clock" >}}-Qualität, entscheidet die niedrigste {{< tooltip "MAC" >}}-Adresse.  
{{< tooltip "Switches" "Switch">}} werden dabei gegenüber {{< tooltip "Endstations" "Endstation" >}} bevorzugt.

<!-- After the election process, the {{< tooltip "GM">}} provides its time to all network participants. -->
Nach dem Wahlprozess verteilt der {{< tooltip "GM" >}} seine {{< termbase "Network Time" >}} an alle Teilnehmer im {{< termbase "Network" >}}.

<!-- ## Network Clock Device Synchronization -->
## Gerätesynchronisation im {{< termbase "Network" >}}

<!-- In {{< tooltip "gPTP" >}}, synchronization occurs at the ports of network devices, allowing for more accurate time measurements and reducing the effects of network delays and jitter. -->
Bei {{< tooltip "gPTP" >}} erfolgt die {{< termbase "Synchronization" >}} direkt an den {{< termbase "Port" >}}s der Netzwerkgeräte.  
Dadurch werden die Zeitmessungen präziser, und der Einfluss von {{< termbase "Network Delay" >}} und {{< termbase "Jitter">}} wird reduziert.

<!-- Hier gehts bei ChatGPT weiter -->

<!-- The Peer Delay is measured by sending a _PDelay Request_ to a neighbor and recording the time it takes to receive a _PDelay Response_. By also including timestamps of when the response was sent and received, the protocol can accurately calculate the link delay between two peers. -->
Das {{< termbase "Peer Delay">}} wird gemessen, indem ein {{< termbase "Pdelay Request">}} an den benachbarten {{< termbase "Port">}} gesendet wird. Dann wird die Zeit gemessen, bis die {{< termbase "Pdelay Response">}} vom benachbarten {{< termbase "Port">}} zurückgesendet wird. Da die {{< termbase "Pdelay Response">}} auch die Zeitstempel enthält, wann die Antwort gesendet bzw. empfangen wurde, kann mit {{< tooltip "gPTP">}} die {{< termbase "Delay">}} zwischen zwei benachparten {{< termbase "Ports">}} präzise gemessen werden.

<!-- {{< figure src="/images/gPTP-sync.drawio.svg" alt="Port to Port sync" fig-num="1" title="gPTP sync process is Port to Port" id="fig-gPTP-sync">}} -->
{{< figure src="/images/gPTP-sync.drawio.svg" alt="Port to Port synchronisation" fig-num="1" title="Bei gPTP wird von Port zu Port synchronisiert" id="fig-gPTP-sync">}}

<!-- This contrasts with PTPv1, which uses the end-to-end approach that may introduce additional uncertainties in time synchronization due to varying network conditions. -->
Dies steht im Kontrast zu PTPv1. Bei PTPv1 wird ein {{< termbase "End To End">}} Ansatz gewählt, der die oben genannten Unsicherheiten wie {{< termbase "Network Delay">}} und {{< termbase "Jitter">}} nicht ausreichend berücksichtigen kann.

<!-- {{< figure src="/images/PTPv1-sync.drawio.svg" alt="Port to Port sync" fig-num="2" title="PTPv1 sync process is End to End" id="fig-gPTP-sync">}} -->
{{< figure src="/images/PTPv1-sync.drawio.svg" alt="Port to Port sync" fig-num="2" title="Bei PTPv1 wird Ende-zu-Ende synchronisiert" id="fig-gPTP-sync">}}

<!-- ## Network Time Domain -->
## Die {{< termbase "Network Time">}}

<!-- All devices synchronized to the same {{< tooltip "gPTP" >}} GrandMaster belong to a single domain. Each domain is exclusively clocked by one {{< tooltip "gPTP" >}} {{< tooltip "GM">}}. In {{< tooltip "Milan">}}, audio streams cannot be shared between different {{< tooltip "gPTP" >}} domains because there is no timing relationship between them. -->
Alle Geräte die auf den gleichen {{< tooltip "gPTP">}} {{< termbase "Grandmaster">}} synchronisieren, gehören zur gleichen Zeit-{{< termbase "Domain">}}. Bei Milan können {{< termbase "Streams">}} nicht zwischen unterschiedlichen {{< tooltip "gPTP">}} {{< termbase "Domains">}} geteilt werden, da es keinen zeitlichen Zusammenhang zwischen unterschiedlichen {{< termbase "Domains">}} gibt.

<!-- ## Media Time -->
## Der {{< termbase "Media Time">}}

<!-- To ensure accurate playback and recording, {{< tooltip "Endstations" "Endstation" >}} must synchronize the timing of their audio playback/recording to the shared {{< tooltip "Network Time" >}}. This synchronization is called Media Time. -->
Um eine genaue Audio-{{< termbase "Playback">}} und -{{< termbase "Recording">}} {{< termbase "Sampling">}} zu gewährleisten, müssen {{< tooltip "Endstations" "Endstation">}} ihre Audio-{{< termbase "Playback">}} und {{< termbase "Recording">}} {{< termbase "Clock" >}} auf die gleiche {{< termbase "Network Time">}} synchronisiert werden. Diese Art der Synchronisation nennen wir {{< termbase "Media Time">}}

<!-- Media Time can be achieved in two ways: by locking to the timing information in an Audio {{< tooltip "Stream" >}}, or by using a Clock Reference Format (CRF) Stream. Both methods allow devices to align their local audio clocks with the rest of the network. More details on the Media formats can be found in [Media Transport](../01_media-transport/_index.md). -->
Der {{< termbase "Media Time">}} kann auf zwei Arten sichergestellt werden: Synchronisation auf die {{< termbase "Timing">}} Informationen in einem {{< tooltip "Stream">}} oder durch die Benutzung eines Clock Reference Formats (CRF) {{< termbase "Streams">}}. Beide Methoden erlauben es den {{< tooltip "Endstations" "Endstation">}} ihre lokale {{< termbase "Clock">}} mit dem Rest des {{< termbase "Network">}}s zu synchronisieren. Mehr Infos zu den verschiedenen Medien Formaten gibt es im Kapitel [Datenübertragung](../01_media-transport/_index.md).

<!-- Support for {{< tooltip "CRF" >}} is optional and depends on the device capabilities. Smaller devices often rely on {{< tooltip "AAF">}} streams alone for their {{< termbase "Media Time">}}. -->
Nicht alle Geräte unterstützen {{< tooltip "CRF">}}. Kleinere Geräte benötigen oft nur den {{< tooltip "AAF">}} {{< termbase "Stream">}} für ihren {{< termbase "Media Time">}}.