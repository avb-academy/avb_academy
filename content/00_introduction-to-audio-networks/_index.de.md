---
title: "Audionetzwerk Intro"
date: 2025-02-11
weight: 1
---

<!-- {{% notice info %}}
- Audio networks are used to transmit digital audio data between devices connected in the same network.
- Typically, there are three traffic types in an audio network
    - [Clock Data](clock_data): Ensures correct operation of the entire audio systems
    - [Audio Data](audio_data): Digital representation of the analog signal. With a tight real-time requirement.
    - [Control Data](control_data): Set up and monitor the system. Less real-time constraint.
- In Milan AVB, a Stream is used to send data from a source to a destination. Stream formats are defined by the Milan specification. All Streams are multicast, meaning they do not consume additional bandwidth if connected to multiple destinations.
{{% /notice %}} -->
{{% notice info%}}
- Audionetzwerke übertragen digitale Audiodaten zwischen Geräten innerhalb desselben Netzwerks.  
- Typischerweise gibt es drei Arten von Netzwerk-Daten in einem Audionetzwerk:  
    - [Taktdaten](clock_data): Sorgen dafür, dass das gesamte System synchron arbeitet.  
    - [Audiodaten](audio_data): Digitale Repräsentation eines analogen Signals. Diese Daten haben besonders hohe {{< termbase "Real Time">}}-Anforderungen.  
    - [Steuerdaten](control_data): Unterstützen Konfiguration und Monitoring des Systems. Ihre {{< termbase "Real Time">}}-Anforderungen sind geringer.  
- In einem Milan AVB {{< termbase "Network">}} werden {{< termbase "Streams">}} benutzt um Daten zwischen Quelle und Senke übertragen. Das Format der Streams ist in der Milan-Spezifikation definiert. Alle {{< termbase "Streams">}} werden als Multicast-Streams gesendet. Das spart Bandbreite, wenn ein {{< termbase "Stream">}} an mehrere Empfänger geht.
{{% /notice %}}

<!-- Consider the following scenario: A microphone is connected to a stage box. The stage box transmits digital audio to the mixing console. The transmission often uses an audio network, as illustrated [Fig. 1](#fig-audio-setup). -->
[Abb. 1](#fig-audio-setup) zeigt ein einfaches Setup für eine Audioübertragung. Ein {{< termbase "Microphone">}} ist mit einer {{< termbase "Stage Box">}} verbunden. Diese sendet das digitale Audiosignal an ein {{< termbase "Mixing Console">}}. Die Übertragung erfolgt dabei häufig über ein Audionetzwerk.

<!-- {{< figure src="/images/audio-setup.drawio.svg" alt="Typical audio setup" fig-num="1" title="Exemplary stage setup that includes all relevant components for an audio network" id="fig-audio-setup">}} -->
{{< figure src="/images/audio-setup.drawio.svg" alt="Typical audio setup" fig-num="1" title="Beispielhaftes Setup dass alle Komponenten eines Audionetzwerks enthält" id="fig-audio-setup">}}

<!-- The microphone is connected to an input of the stage box using a XLR cable ([Fig. 1](#fig-audio-setup), No. 1). The loudspeaker is connected to an output of the stage box with an appropriate cable ([Fig. 1](#fig-audio-setup), No. 2), depending on whether there is a separate amplifier in the loop or not. The details are out of scope for this description. The intention here is to describe an input path and an output path. -->
Das {{< termbase "Microphone">}} ist über ein XLR-{{< termbase "Cable">}} mit einem Eingang der {{< termbase "Stage Box">}} verbunden ([Abb. 1](#fig-audio-setup), Nr. 1). Ein Lautsprecher ist über ein geeignetes {{< termbase "Cable">}} mit einem Ausgang der {{< termbase "Stage Box">}} verbunden ([Abb. 1](#fig-audio-setup), Nr. 2). Dieses einfache Beispiel beschreibt lediglich einen grundlegenden Signalfluss vom Eingang zum Ausgang. In der Praxis sind solche Verbindungen oft komplexer, doch dieses Setup genügt, um das Grundprinzip von Audionetzwerken zu veranschaulichen.

<!-- The connection between the stage box and the mixing console is made with network cables. It is a common practice to use a redundant connection featuring a {{< tooltip "Primary">}} ([Fig. 1](#fig-audio-setup), No. 3) and {{< tooltip "Secondary">}} ([Fig. 1](#fig-audio-setup), No. 4) port (labeled with P/S) to enhance operational security. The redundant connection is an optional feature and might not always be provided by a networked audio device. -->
Die Verbindung zwischen der {{< termbase "Stage Box">}} und dem {{< termbase "Mixing Console">}} erfolgt über {{< termbase "Network">}}kabel. In der Praxis wird häufig eine redundante Verbindung mit einem {{< tooltip "Primary">}}- ([Abb. 1](#fig-audio-setup), Nr. 3) und einem {{< tooltip "Secondary">}}-{{< termbase "Port">}} ([Abb. 1](#fig-audio-setup), Nr. 4) verwendet, die mit P/S gekennzeichnet sind, um die Betriebssicherheit zu erhöhen. Eine solche Redundanz ist optional und wird nicht von allen {{< termbase "Networked Audio">}}-Geräten unterstützt.

<!-- The {{< tooltip "Secondary">}} port “mirrors” the data {{< tooltip "Primary">}} port. The description in the following will not distinguish between the two ports. -->
Der {{< tooltip "Secondary">}}-{{< termbase "Port">}} spiegelt die Daten des {{< tooltip "Primary">}}-{{< termbase "Ports">}}. In den folgenden Beschreibungen wird daher nicht zwischen den beiden {{< termbase "Ports">}} unterschieden.

<!-- The relevant traffic of an audio network can be categorized into three different data types: Clock Data, Audio Data and Control Data. All signals in the audio network are digital signals. The general principle is shown in [Fig. 2](#fig-traffic-components-all). -->
Die Daten in einem {{< termbase "Networked Audio">}} lassen sich in drei Kategorien unterteilen: {{< termbase "Clock">}}-, Audio- und {{< termbase "Control">}}s-Daten. Alle Signale in einem {{< termbase "Networked Audio">}} sind digital. Das Grundprinzip ist in [Abb. 2](#fig-traffic-components-all) dargestellt.

<!-- {{< figure src="/images/traffic-components-all.drawio.svg" alt="Three main traffic components in an audio network" fig-num="2" title="Three main traffic components in an audio network" id="fig-traffic-components-all">}} -->

{{< figure src="/images/traffic-components-all.drawio.svg" alt="Three main traffic components in an audio network" fig-num="2" title="Die drei Hauptkomponenten eines Audio Netzwerks" id="fig-traffic-components-all">}}. 

<!-- 
{{% notice tip %}}
Prefer a less technical explanation?
Visit [milanav.com/about](https://milanav.com/about) for a broader perspective.
{{% /notice %}} -->

{{% notice tip %}}
Du bevorzugst eine weniger technische Erklärung?  
Besuche [milanav.com/about](https://milanav.com/about) für allgemeinere Informationen.
{{% /notice %}}
