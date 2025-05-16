---
title: "Network Timing"
date: 2025-02-11
weight: 1
---

{{% notice info %}}
- A Milan network has one clock leader. The {{< tooltip "BTCA">}} is executed automatically each time a change in the network occurs to elect a GrandMaster (GM).
- The {{< tooltip "GM">}} is elected based on parameters that describe the clock quality of the device. The best quality wins.
- Network Time is the shared global time base provided to all devices in the network by {{< tooltip "gPTP">}}.
- Media Time is the timing domain used specifically to synchronize audio recording and playback clocks in Endstations.
{{% /notice %}}

Having a well-synchronized network is crucial for the performance of the network. An unsynchronized network could lead to sampling signals at different points in time. In a less severe scenario, this can result in mixed signals that exhibit a comb filter characteristic, distorting the audio. In a worst-case scenario, the lack of synchronization could cause audio dropouts, glitches, and clicks, significantly degrading the listening experience. Therefore, maintaining precise synchronization is essential to ensure seamless and high-quality audio transmission across the network.

Milan employs the Generalized Precision Timing Protocol (gPTP) to synchronize all participants within the network, including both Endstations and switches. Notably, the inclusion of Switches distinguishes Milan from other existing networked audio protocols, as it requires the Switches to be time-aware and therefore capable of understanding Network time.

Milan timing is divided into two parts: the {{< tooltip "Network Time">}}, provided to all participants of the network via {{< tooltip "gPTP" >}}, and the timing information that controls the audio sampling clock, referred to as {{< tooltip "Media Time">}}. To avoid confusion between the two domains, these terms clearly distinguish global synchronization from audio-specific clock control.

## Network Clock Leader Election

<div class="text-image-container">
  <div class="text">
    <p>Consider a Milan network that has just been switched on. It is likely that it consists of multiple {{< tooltip "Endstations">}} and {{< tooltip "Switches" "Switch">}}. In a first step, a Grand Master (GM) has to be elected. This Grand Master will distribute its time to all participants allowing them to share a common understanding of time. The election process is defined in an algorithm called Best Time Transmitter Algorithm (BTCA). The algorithm is executed automatically when a change in the network is detected.</p>
  </div>
  <div class="image">
    <img src="/images/gPTP-BTCA.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

The election of the the {{< tooltip "gPTP" >}} GrandMaster is based on parameters that describe the clock quality of the device. Of course the best clock quality is elected as the {{< tooltip "GM">}}. In case multiple devices have the same clock quality, the device with the lowest {{< tooltip "MAC" >}} address is selected. Switches are preferred over Endstations.
  
After the election process, the {{< tooltip "GM">}} provides its time to all network participants.

## Network Clock Device Synchronisation

In {{< tooltip "gPTP" >}}, synchronization occurs at the ports of network devices, allowing for more accurate time measurements and reducing the effects of network delays and jitter.

The Peer Delay is measured by sending a _PDelay Request_ to a neighbor and recording the time it takes to receive a _PDelay Response_. By also including timestamps of when the response was sent and received, the protocol can accurately calculate the link delay between two peers.

{{< figure src="/images/gPTP-sync.drawio.svg" alt="Port to Port sync" fig-num="1" title="gPTP sync process is Port to Port" id="fig-gPTP-sync">}}

This contrasts with PTPv1, which uses the end-to-end approach that may introduce additional uncertainties in time synchronization due to varying network conditions.

{{< figure src="/images/PTPv1-sync.drawio.svg" alt="Port to Port sync" fig-num="2" title="PTPv1 sync process is End to End" id="fig-gPTP-sync">}}

## Network Clock Domain
All devices synchronized to the same {{< tooltip "gPTP" >}} GrandMaster belong to a single domain. Each domain is exclusively clocked by one {{< tooltip "gPTP" >}} {{< tooltip "GM">}}. In {{< tooltip "Milan">}}, audio streams cannot be shared between different {{< tooltip "gPTP" >}} domains because there is no timing relationship between them.

## Media Clock

To ensure accurate playback and recording, {{< tooltip "Endstations" "Endstation" >}} must synchronize the timing of their audio playback/recording to the shared {{< tooltip "Network Time" >}}. This synchronization is called Media Clocking.

Media Clocking can be achieved in two ways: by locking to the timing information in an {{< tooltip "AAF" >}} {{< tooltip "Stream" >}}, or by using a Clock Reference Format ({{< tooltip "CRF" >}}) stream. Both methods allow devices to align their local audio clocks with the rest of the network.

Support for {{< tooltip "CRF" >}} is optional and depends on the device capabilities. Smaller devices often rely on AAF streams alone for Media Clocking.