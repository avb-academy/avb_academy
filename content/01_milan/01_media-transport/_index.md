---
title: "Media Transport"
date: 2025-02-11
weight: 2
---

{{% notice info %}}
- Data is encapsulated in {{< tooltip "Streams" "Stream">}} to use available bandwidth more efficiently.
- Audio transport in {{< tooltip "Milan">}}: 32bit {{< tooltip "PCM">}} data.
- Clock Reference Format ({{< tooltip "CRF">}}): Additional media clock information, optional for small devices.
- A {{< tooltip "Stream">}} has a configurable delay in the range of 0.25ms to 2ms.
{{% /notice %}}

## Audio Data

In {{< tooltip "Milan">}} audio data is transmitted via {{< tooltip "Streams" "Stream">}}. The audio transport in {{< tooltip "Milan">}} uses the Audio Video Transmission Protocol ({{< tooltip "AVTP">}}). This protocol specifies the strucuture of the data frames that are tansmitted in the network.

The {{< tooltip "Milan">}} specification utilizes the {{< tooltip "AVTP">}} Audio Format ({{< tooltip "AAF">}}) as the format for audio transmissions. This is not to be confused with the *Advanced Authoring Format*. It specifies that each {{< tooltip "PCM">}} sample is transmitted as a 32-bit value. If a sample has less than 32-bit, it is zero padded.

{{< tooltip "Milan">}} specifies that a {{< tooltip "Talker">}} defines the outgoing {{< tooltip "Stream">}} format. This refers to the number of audio channels that are contained in a {{< tooltip "Stream">}}. The {{< tooltip "Listener">}} has to adapt to the {{< tooltip "Stream">}} format of the {{< tooltip "Talker">}}.

The {{< tooltip "Milan">}} Base Format specifies support for channel counts of either 1, 2, 4, 6, 8 audio channels per {{< tooltip "Stream">}}. The support for the Base Format is mandatory for {{< tooltip "Listeners" "Listener">}} and part of the {{< tooltip "Milan">}} certification. This ensures interoperability between any {{< tooltip "Talker">}} and {{< tooltip "Listener">}}.

<div class="text-image-container">
  <div class="text">
    <p>A {{< tooltip "Stream">}} can be viewed as a container for audio data. In addition to the audio content, it also includes Ethernet information, such as the source and destination {{< tooltip "MAC">}} addresses. Ethernet information is present in every packet. This mandatory overhead for each packet should make it evident that using a larger number of audio channels per {{< tooltip "Stream">}} is more efficient than using a smaller number.</p>
  </div>
  <div class="image">
    <img src="/images/Stream-format.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

It is worth noting that a {{< tooltip "Stream">}} is configured with a fixed delay time before it starts streaming. The value range for delays is from 0.25ms to 2ms. Due to the fact that all devices in the network have a shared understanding of time, it is possible with {{< tooltip "Milan">}} to guarantee the latency that has been configured for the {{< tooltip "Stream">}}. Details on how this is possible are described in [Traffic Shaping Section](../03_traffic-shaping/_index.md).

## Clock Data

The previous section [Network Timing](../00_network-timing/_index.md) has explained the core principle of network time in {{< tooltip "Milan">}}. The {{< tooltip "Milan">}} specification uses an additional clocking mechanism called Clock Reference Format ({{< tooltip "CRF">}}).

This format allows Endstations to synchronize their media clocks to a common nominator. Without going too much into the details, {{< tooltip "CRF">}} adds an additional layer that is related to the gPTP time stamps but allows to generate the actual media clock signal for the audio unit of an Endstation.

The support for {{< tooltip "CRF">}} is dependent on the device capabilities. Especially small devices do not necessarily need to support the {{< tooltip "CRF">}} format. They extract the relevant Media Clock information from the {{< tooltip "AAF">}} Audio {{< tooltip "Stream">}}.