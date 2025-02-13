---
title: "Audio Networks Intro"
date: 2025-02-11
weight: 1
---

{{% notice info %}}
- Audio networks are used to transmit digital audio data between devices connected in the same network.
- Typically, there are three traffic types in an audio network
    - [Clock Data](clock_data): Ensures correct operation of the entire audio systems
    - [Audio Data](audio_data): Digital representation of the analog signal. With a tight real-time requirement.
    - [Control Data](control_data): Set up and monitor the system. Less real-time constraint.
- In Milan, a Stream is used to send data from a source to a destination. Stream formats are defined by the Milan specification. All Streams are multicast, meaning they do not consume additional bandwidth if connected to multiple destinations.
{{% /notice %}}

Consider the following scenario: A microphone is connected to a stagebox. The stagebox transmits digital audio to the mixing console. The transmission often uses an audio network, as illustrated in the following Figure.

{{< figure src="/images/audio-setup.drawio.svg" alt="Typical audio setup" fig-num="1" title="Exemplary stage setup that includes all relevant components for an audio network" id="fig-audio-setup">}}

The microphone is connected to an input of the stagebox using a XLR cable ([Fig. 1](#fig-audio-setup), No. 1). The loudspeaker is connected to an output of the stagebox with an appropriate cable ([Fig. 1](#fig-audio-setup), No. 2), depending on whether there is a separate amplifier in the loop or not. The details are out of scope for this description. The intention here is to describe an input path and an output path.

The connection between the stagebox and the mixing console is made with network cables. It is a common practice to use a redundant connection featuring a {{< tooltip "Primary">}} ([Fig. 1](#fig-audio-setup), No. 3) and {{< tooltip "Secondary">}} ([Fig. 1](#fig-audio-setup), No. 4) port to enhance operational security. The redundant connection is an optional feature and might not always be provided by a networked audio device.

The {{< tooltip "Secondary">}} port “mirrors” the data {{< tooltip "Primary">}} port. The description in the following will not distinguish between the two ports.

The relevant traffic of an audio network can be categorized into three different data types: Clock Data, Audio Data and Control Data. All signals in the audio network are digital signals. The general principle is shown in [Fig. 2](#fig-traffic-components-all).

{{< figure src="/images/traffic-components-all.drawio.svg" alt="Three main traffic components in an audio network" fig-num="2" title="Three main traffic components in an audio network" id="fig-traffic-components-all">}}
