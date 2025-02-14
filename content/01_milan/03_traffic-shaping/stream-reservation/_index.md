---
title: "Stream Reservation Protocol (SRP)"
date: 2025-02-11
weight: 1
---

When a Listener is configured to listen to a specific Talker stream, the {{< tooltip "SRP">}} protocol ensures that the required bandwidth is available on the entire path from the Talker to the Listener. Each switch checks if the bandwidth is available. If a switch has insufficient bandwidth, the stream will not be established.

If {{< tooltip "SRP">}} successfully configures a path from Talker to Listener, the Talker starts streaming its data.

It is important to point out that **up to 75%** of the available bandwidth **can** be utilized for Milan. It is not reserved per se. If a stream only needs 2% of the available bandwidth, then only these 2% are reserved, and the rest remains available for other traffic.

## How much traffic is reserved for my audio stream?

The following table provides a quick guide on how much bandwidth is reserved for different combinations of channels and sample rates.

<table>
  <thead>
    <tr>
      <th># Channels</th>
      <th>48k in Mbit/s</th>
      <th>96k in Mbit/s</th>
      <th>192k in Mbit/s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5.82</td>
      <td>7.36</td>
      <td>10.43</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7.36</td>
      <td>10.43</td>
      <td>16.58</td>
    </tr>
    <tr>
      <td>4</td>
      <td>10.43</td>
      <td>16.58</td>
      <td>28.86</td>
    </tr>
    <tr>
      <td>6</td>
      <td>13.50</td>
      <td>22.72</td>
      <td>41.15</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16.58</td>
      <td>28.86</td>
      <td>53.44</td>
    </tr>
    <tr>
      <td colspan="4"></td> <!-- Empty line above the CRF stream -->
    </tr>
    <tr>
      <td>CRF</td>
      <td colspan="3">always 5.63Mbit/s</td> <!-- Combined cell for CRF -->
    </tr>
  </tbody>
</table>


## Detailed calculation
The calculation is described in detail in the respective {{< tooltip "IEEE">}} specifications and is not explained further here.
Follow these steps to calculate the bandwidth required for a given stream configuration
{{% button href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" icon="download" %}}Download MSRP Details Cheat Sheet{{% /button %}}


<div class="inline-images">
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank">
    <img src="/msrp_milan_cheat_sheet/msrp_details-AVTP.drawio.svg" alt="Calculation steps for Milan"/>
  </a>
  <a href="/msrp_milan_cheat_sheet/msrp_details.drawio.pdf" target="_blank">
    <img src="/msrp_milan_cheat_sheet/msrp_details-CRF.drawio.svg" alt="Calculation steps for CRF"/>
  </a>
</div>
