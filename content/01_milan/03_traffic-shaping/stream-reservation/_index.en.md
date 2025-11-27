---
title: "Stream Reservation Protocol (SRP)"
date: 2025-02-11
weight: 1
---

When a {{< tooltip "Listener">}} is configured to listen to a specific {{< tooltip "Talker">}} {{< tooltip "Stream">}}, the {{< termbase "Stream Reservation Protocol">}} (SRP) ensures that the required bandwidth is available on the entire path from the Talker to the Listener. Each {{< tooltip "Switch">}} checks if the bandwidth is available. If a switch has insufficient bandwidth, the stream will not be established.

If {{< tooltip "SRP">}} successfully configures a path from Talker to Listener, the Talker starts streaming its data.

It is important to point out that **up to 75%** of the available bandwidth **can** be utilized for Milan AVB. It is not reserved per se. If a stream only needs 2% of the available bandwidth, then only these 2% are reserved, and the rest remains available for other traffic.

## How much bandwidth is reserved for my audio stream?

The following table provides a quick guide on how much bandwidth is reserved for different combinations of channels and sample rates.

<a href="/msrp_milan_cheat_sheet/msrp_summary.drawio.pdf" target="_blank" class="highlight no-triangle">
<img src="/msrp_milan_cheat_sheet/msrp_summary.drawio.svg" alt="Overview combination sample rate - channel count"/>
</a>

## Detailed calculation
The following section summarizes the calculation described in the respective {{< tooltip "IEEE">}} specifications.  
Follow these steps to calculate the bandwidth required for a given stream configuration
{{% button href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" icon="download" class="no-triangle"%}}Download MSRP Details Cheat Sheet{{% /button %}}


<div class="inline-images">
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-AVTP.drawio.svg" alt="Calculation steps for Milan"/>
  </a>
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank" class="highlight no-triangle">
    <img src="/msrp_milan_cheat_sheet/msrp_details-CRF.drawio.svg" alt="Calculation steps for CRF"/>
  </a>
</div>
