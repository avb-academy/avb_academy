---
title: "Stream Reservation Protocol (SRP)"
date: 2025-02-11
weight: 1
---

<!-- When a {{< tooltip "Listener">}} is configured to listen to a specific {{< tooltip "Talker">}} {{< tooltip "Stream">}}, the {{< termbase "Stream Reservation Protocol">}} (SRP) ensures that the required bandwidth is available on the entire path from the Talker to the Listener. Each {{< tooltip "Switch">}} checks if the bandwidth is available. If a switch has insufficient bandwidth, the stream will not be established. -->
Wenn ein {{< tooltip "Listener">}} so konfiguriert ist, dass er einem bestimmten {{< tooltip "Talker">}}-{{< tooltip "Stream">}} zuhört, stellt das {{< termbase "Stream Reservation Protocol">}} (SRP) sicher, dass die erforderliche {{< termbase "Bandwidth">}} auf dem gesamten Übertragungsweg zwischen Talker und Listener verfügbar ist. Jeder {{< tooltip "Switch">}} prüft dabei, ob genügend {{< termbase "Bandwidth">}} vorhanden ist. Kann ein Switch die benötigte {{< termbase "Bandwidth">}} nicht bereitstellen, wird der entsprechende {{< termbase "Stream">}} nicht aufgebaut.

<!-- If {{< tooltip "SRP">}} successfully configures a path from Talker to Listener, the Talker starts streaming its data. -->
Wenn das {{< termbase "Stream Reservation Protocol">}} den Übertragungsweg vom {{< termbase "Talker">}} zum {{< termbase "Listener">}} erfolgreich eingerichtet hat, beginnt der Talker mit dem {{< termbase "Streaming">}} der Audiodaten.

<!-- It is important to point out that **up to 75%** of the available bandwidth **can** be utilized for Milan AVB. It is not reserved per se. If a stream only needs 2% of the available bandwidth, then only these 2% are reserved, and the rest remains available for other traffic. -->
Es ist wichtig hervorzuheben, dass **bis zu 75 %** der verfügbaren {{< termbase "Bandwidth">}} für Milan AVB genutzt werden **können**. Diese wird jedoch nicht pauschal reserviert und blockiert somit nicht den übrigen {{< termbase "Network Traffic">}}. Benötigt ein {{< termbase "Stream">}} beispielsweise nur 2 % der verfügbaren {{< termbase "Bandwidth">}}, wird genau dieser Anteil reserviert, während die verbleibende {{< termbase "Bandwidth">}} für anderen {{< termbase "Network Traffic">}} frei bleibt.

<!-- ## How much traffic is reserved for my audio stream? -->
## Bandbreitenreservierung für Audio-{{< termbase "Streams">}}

<!-- The following table provides a quick guide on how much bandwidth is reserved for different combinations of channels and sample rates. -->
Die folgende Tabelle zeigt, wie viel {{< termbase "Bandwidth">}} für unterschiedliche Kombinationen aus Kanalanzahl und {{< termbase "Sample Rate">}} reserviert wird.

<!-- <a href="/msrp_milan_cheat_sheet/msrp_summary.drawio.pdf" target="_blank" class="highlight no-triangle">
<img src="/msrp_milan_cheat_sheet/msrp_summary.drawio.svg" alt="Calculation steps for Milan"/>
</a> -->
<a href="/msrp_milan_cheat_sheet/msrp_summary.drawio.pdf" target="_blank" class="highlight no-triangle">
<img src="/msrp_milan_cheat_sheet/msrp_summary.drawio.svg" alt="Übersicht der Reservierung der Kanalanzahl–Sample-Rate-Kombination"/>
</a>

<!-- ## Detailed calculation -->
## Bandbreitenberechnung im Detail

<!-- The following section summarizes the calculation described in the respective {{< tooltip "IEEE">}} specifications. -->
<!-- Follow these steps to calculate the bandwidth required for a given stream configuration -->
Die folgende Darstellung fasst die in den {{< tooltip "IEEE">}}-Spezifikationen beschriebene Berechnung zusammen und zeigt die Schritte zur Bestimmung der benötigten {{< termbase "Bandwidth">}} für eine gegebene {{< termbase "Stream">}}-Konfiguration.

<!-- {{% button href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" icon="download" class="no-triangle"%}}Download MSRP Details Cheat Sheet{{% /button %}} -->
{{% button href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" icon="download" class="no-triangle"%}}Download MSRP Details Cheat Sheet{{% /button %}}

<!-- <div class="inline-images">
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-AVTP.drawio.svg" alt="Calculation steps for Milan"/>
  </a>
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-CRF.drawio.svg" alt="Calculation steps for CRF"/>
  </a>
</div> -->
<div class="inline-images">
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-AVTP.drawio.svg" alt="Berechnungsschritte für Milan"/>
  </a>
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-CRF.drawio.svg" alt="Berechnungsschritte für CRF"/>
  </a>
</div>
