---
title: "Stream Reservation Protocol (SRP)"
date: 2025-02-11
weight: 1
---

<!-- When a Listener is configured to listen to a specific Talker stream, the {{< tooltip "SRP">}} protocol ensures that the required bandwidth is available on the entire path from the Talker to the Listener. Each switch checks if the bandwidth is available. If a switch has insufficient bandwidth, the stream will not be established. -->
Wenn ein {{< tooltip "Listener">}} so konfiguriert ist, dass er einem bestimmten {{< tooltip "Talker">}}-{{< tooltip "Stream">}} zuhört, stellt das {{< termbase "Stream Reservation Protocol">}} sicher, dass die erforderliche {{< termbase "Bandwidth">}} auf dem gesamten Übertragungsweg zwischen Talker und Listener verfügbar ist. Jeder {{< tooltip "Switch">}} überprüft dabei, ob ausreichend {{< termbase "Bandwidth">}} vorhanden ist. Kann ein Switch nicht genügend {{< termbase "Bandwidth">}} bereitstellen, wird der entsprechende {{< termbase "Stream">}} nicht aufgebaut.

<!-- If {{< tooltip "SRP">}} successfully configures a path from Talker to Listener, the Talker starts streaming its data. -->
Wenn das {{< termbase "Stream Reservation Protocol">}} den Übertragungsweg vom {{< termbase "Talker">}} zum {{< termbase "Listener">}} erfolgreich konfiguriert hat, beginnt der Talker mit dem {{< termbase "streaming">}} der Audiodaten.
<!-- It is important to point out that **up to 75%** of the available bandwidth **can** be utilized for Milan AVB. It is not reserved per se. If a stream only needs 2% of the available bandwidth, then only these 2% are reserved, and the rest remains available for other traffic. -->
Es ist wichtig hervorzuheben, dass **bis zu 75%** der verfügbaren {{< termbase "Bandwidth">}} für Milan AVB genutzt werden **können**. Diese wird jedoch nicht pauschal reserviert und damit auch nicht für anderen {{< termbase "Network Traffic">}} blockiert. Benötigt ein {{< termbase "Stream">}} beispielsweise nur 2% der verfügbaren {{< termbase "Bandwidth">}}, so wird auch nur genau dieser Anteil reserviert. Die verbleibende {{< termbase "Bandwidth">}} steht jedem anderem {{< termbase "Network Traffic">}} zur Verfügung.

<!-- ## How much traffic is reserved for my audio stream? -->
## Bandbreitenreservierung für Audio-{{< termbase "Streams">}}
<!-- The following table provides a quick guide on how much bandwidth is reserved for different combinations of channels and sample rates. -->
Die folgende Tabelle zeigt, wie viel {{< termbase "Bandwidth">}} für unterschiedliche Kombinationen aus Kanalanzahl und {{< termbase "Sample Rate">}} reserviert wird.

<!-- <a href="/msrp_milan_cheat_sheet/msrp_summary.drawio.pdf" target="_blank" class="highlight no-triangle">
<img src="/msrp_milan_cheat_sheet/msrp_summary.drawio.svg" alt="Calculation steps for Milan"/>
</a> -->
<a href="/msrp_milan_cheat_sheet/msrp_summary.drawio.pdf" target="_blank" class="highlight no-triangle">
<img src="/msrp_milan_cheat_sheet/msrp_summary.drawio.svg" alt="Übersicht der Reserverierung der Kanalanzahl - Sample Rate Kombination."/>
</a>

<!-- ## Detailed calculation -->
## Bandbreitenberechnung im Detail
<!-- The calculation is described in detail in the respective {{< tooltip "IEEE">}} specifications and is not explained further here. -->
<!-- Follow these steps to calculate the bandwidth required for a given stream configuration -->
Die folgende Darstellung fasst die in den {{< tooltip "IEEE">}}-Spezifikationen beschriebene Berechnung zusammen.  
Mit den folgenden Schritten lässt sich die benötigte {{< termbase "Bandwidth">}} für eine gegebene {{< termbase "Stream">}}-Konfiguration berechnen.
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
