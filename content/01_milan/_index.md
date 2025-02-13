---
title: "Milan"
date: 2025-02-11
weight: 2
---

{{% notice info %}}
-  Endstation: A device that either converts audio into Milan (Talker), or from Milan into audio (Listener). The Talker/Listener functionality can be combined in the same device. All Endstations are Milan certified
- Switch: A device that forwards Streams from Talkers to Listeners and usually is the gPTP Grandmaster.
- Milan operates on OSI layer 2. Therefore, all addressing is done with MAC addresses.
{{% /notice %}}

Milan is based on a set of IEEE specifications. As explained in the [Introduction](../_index.md#milan-the-proav-flavor-of-avb), Milan is a tightly constrained specfication that is tailored to the needs of the ProAV industry.

To enhance readability, this chapter minimizes the use of technical terms and references. The content is organized by the logical functions of an audio network transmission. The unique features of Milan are explained with minimal technical detail to ensure clarity.

## Milan terms
Have a look at [Fig. 1](#fig-milan-names) which shows the general naming scheme in a Milan network. The terms are explained in the following.

{{< figure src="/images/milan-names.drawio.svg" alt="Milan Names" fig-num="1" title="Milan Names" id="fig-milan-names">}}

### Endstation
A device that converts audio from or into the Milan network. Endstations can contain either Talker or Listener functionality or contain both. Endstations are Milan certified.

### Talker
A Talker converts an audio signal into the network. Could be a digital microphone or a stagebox.

### Listener
A Listener extracts an audio signal from the network. Could be an amplifier.

### Switch
A Switch forwards streams from a Talker to a Listener. Usually, a Switch is the gPTP (GM) in a network. Switches are AVB certified.

### Bridged Endstation
A Bridged Endstation incorporates the Talker and or Listener functionality as well as the Switch functionality.

## OSI layers
Milan operates on Open Systems Interconnection ({{< tooltip "OSI layer">}}) 2. Meaning there is no need for IP addresses. All addressing in Milan is done via Medium Access Control ({{< tooltip "MAC">}}) addresses.
