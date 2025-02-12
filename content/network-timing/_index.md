---
title: "Network Timing"
date: 2025-02-11
weight: 2
---

Having a well-synchronized network is crucial for the performance of the network. An unsynchronized network could lead to sampling signals at different points in time. In a less severe scenario, this can result in mixed signals that exhibit a comb filter characteristic, distorting the audio. In a worst-case scenario, the lack of synchronization could cause audio dropouts, glitches, and clicks, significantly degrading the listening experience and likely displeasing your audience. Therefore, maintaining precise synchronization is essential to ensure seamless and high-quality audio transmission across the network.

{{% notice info %}}
- A Milan network has one clock leader. The BTCA is executed automatically each time a change in the network occurs to elect a GrandMaster (GM).
- The GM is elected based on parameters that describe the clock quality of the device. The best quality wins.
- Switches are preferred over a Bridged Endstation
- Synchronization between participants is done from port to port. This reduces effects of variation in the network.
{{% /notice %}}

Milan employs the Generalized Precision Timing Protocol ({{< tooltip "gPTP" >}}) to synchronize all participants within the network, including both Endstations and switches. Notably, the inclusion of Switches distinguishes Milan from other existing networked audio protocols, as it requires the Switches to be time-aware and therfore capable of understanding network time.

## Clock Leader Election

<div class="text-image-container">
  <div class="text">
    <p>Consider a Milan network that has just been switched on. It is likely that it consists of multiple {{< tooltip "Endstations">}} and {{< tooltip "Switches">}}. In a first step, a Grand Master ({{< tooltip "GM">}}) has to be elected. This Grand Master will distribute its time to all participants allowing them to share a common understanding of time. The election process is defined in an algorithm called Best Time Transmitter Algorithm ({{< tooltip "BTCA">}}). The algorithm is executed automatically when a change in the network is detected.</p>
  </div>
  <div class="image">
    <img src="/images/gPTP-BTCA.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

The election of the the {{< tooltip "gPTP" >}} GrandMaster ({{< tooltip "GM">}}) is based on parameters that describe the clock quality of the device. Of course the best clock quality is elected as the GM. In case multiple devices have the same clock quality, the device with the lowest {{< tooltip "MAC" >}} address is selected. Switches are preferred over a Bridged Endstation.
  
After the election process, the {{< tooltip "GM">}} provides its time to all network participants.

## Device Synchronisation

<div class="text-image-container">
  <div class="text">
    <p>In {{< tooltip "gPTP" >}}, synchronization occurs at the ports of network devices, allowing for more accurate time measurements and reducing the effects of network delays and jitter. This contrasts with PTPv1, which uses the end-to-end approach that may introduce additional uncertainties in time synchronization due to varying network conditions.</p>
  </div>
  <div class="image">
    <img src="/images/gPTP-sync.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>



## Domain
All devices synchronized to the same {{< tooltip "gPTP" >}} GrandMaster ({{< tooltip "GM">}}) belong to a single domain. Each domain is exclusively clocked by one {{< tooltip "gPTP" >}} {{< tooltip "GM">}}. In Milan, audio streams cannot be shared between different {{< tooltip "gPTP" >}} domains because there is no timing relationship between them.