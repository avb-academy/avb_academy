---
title: "Media Transport"
date: 2025-02-11
weight: 2
---

{{% notice info %}}
- Data is encapsulated in {{< tooltip "Streams" "Stream">}} to use available bandwidth more efficiently.
- Audio transport in {{< tooltip "Milan">}}: 32bit {{< tooltip "PCM">}} data.
- {{< tooltip "Media Time">}} controls playback/recording in relation to the {{< tooltip "Network Time">}}
- A {{< tooltip "Stream">}} has a configurable delay in the range of 0.25ms to 2ms.
- Bandwidth usage of Streams is explained in the [Traffic Shaping](../03_traffic-shaping/stream-reservation/_index.md#how-much-traffic-is-reserved-for-my-audio-stream) section.
{{% /notice %}}

## Audio Data

In {{< tooltip "Milan">}}, audio data is transmitted via {{< tooltip "Streams" "Stream">}} using the Audio Video Transmission Protocol ({{< tooltip "AVTP">}}), which defines the structure of the data frames sent across the network.

The specification adopts the AVTP Audio Format (AAF) for audio transport—not to be confused with the Advanced Authoring Format. It mandates that each {{< tooltip "PCM">}} sample be transmitted as a 32-bit value, with shorter samples zero-padded as needed.

A {{< tooltip "Talker">}} in a {{< tooltip "Milan">}} network defines the outgoing {{< tooltip "Stream">}} format, specifying the number of audio channels in the {{< tooltip "Stream">}}. The {{< tooltip "Listener">}} is required to adapt to the format provided by the {{< tooltip "Talker">}}.

The {{< tooltip "Milan">}} Base Format specifies support for channel counts of either 1, 2, 4, 6, 8 audio channels per {{< tooltip "Stream">}}. The support for the Base Format is mandatory for {{< tooltip "Listeners" "Listener">}} and part of the {{< tooltip "Milan">}} certification. This ensures interoperability between any {{< tooltip "Talker">}} and {{< tooltip "Listener">}}.

<div class="text-image-container">
  <div class="text">
    <p>A {{< tooltip "Stream">}} can be viewed as a container for audio data. In addition to the audio content, it also includes Ethernet information, such as the source and destination {{< tooltip "MAC">}} addresses. Ethernet information is present in every packet. This mandatory overhead for each packet should make it evident that using a larger number of audio channels per {{< tooltip "Stream">}} is more efficient than using a smaller number.</p>
  </div>
  <div class="image">
    <img src="/images/stream-format.drawio.svg" alt="Image" style="max-width: 100%; height: auto;">
  </div>
</div>

It is worth noting that a {{< tooltip "Stream">}} is configured with a fixed delay time before it starts streaming. The value range for delays is from 0.25ms to 2ms. Due to the fact that all devices in the network have a shared understanding of time, it is possible with {{< tooltip "Milan">}} to guarantee the latency that has been configured for the {{< tooltip "Stream">}}. Details on how this is possible are described in [Traffic Shaping Section](../03_traffic-shaping/_index.md).

## Media Clock Data

The previous section [Network Timing](../00_network-timing/_index.md) explains the distinction between {{< tooltip "Network Time">}} and {{< tooltip "Media Time">}} in {{< tooltip "Milan">}}.

In summary:

- **Network Time** is the shared global time base provided to all devices in the network by {{< tooltip "gPTP">}}.
- **Media Time** is the timing domain used specifically to synchronize audio recording and playback clocks in Endstations.

From a transport perspective, a {{< tooltip "Stream">}} can carry either Network Time synchronization data or Media Time clocking data.
