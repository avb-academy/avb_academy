---
title: "Milan AVB"
date: 2025-02-11
weight: 2
---

<!-- {{% notice info %}}
-  Endstation: A device that either converts audio into Milan (Talker), or from Milan into audio (Listener). The Talker/Listener functionality can be combined in the same device. All Endstations are Milan certified
- Switch: A device that forwards Streams from Talkers to Listeners and usually is the gPTP Grandmaster.
- Milan operates on OSI layer 2. Therefore, all addressing is done with MAC addresses.
{{% /notice %}} -->
{{% notice info %}}
- Endstation: Ein Gerät, das Audio in das Milan-Format umwandelt ({{< termbase "Talker">}}) oder Netzwerk-Signale in Audio zurückwandelt ({{< termbase "Listener">}}). Manche Geräte kombinieren beide Funktionen.
- Switch: Ein Gerät, das Pakete zwischen {{< termbase "Ports">}} weiterleitet.
- Milan arbeitet auf OSI {{< termbase "Layer" >}} 2, daher erfolgt die Adressierung ausschließlich über MAC-Adressen.
{{% /notice %}}

<!-- Milan AVB is based on a set of IEEE specifications. As explained in the [Introduction](../_index.md#milan-the-proav-flavor-of-avb), Milan is a tightly constrained specification that is tailored to the needs of the ProAV industry. -->
Milan AVB basiert auf einer Reihe von {{< tooltip "IEEE">}}-Spezifikationen. Wie bereits in der [Einleitung](../_index.md#milan-der-proav-flavor-von-avb) erläutert, ist Milan ein klar definierter Standard, der gezielt auf die Bedürfnisse der ProAV-Branche zugeschnitten wurde.

<!-- To enhance readability, this chapter minimizes the use of technical terms and references. The content is organized by the logical functions of an audio network transmission. The unique features of Milan are explained with minimal technical detail to ensure clarity. -->
Dieses Kapitel ist so gestaltet, dass es leicht verständlich ist. Technische Begriffe und Quellenangaben werden daher möglichst sparsam verwendet. Der Inhalt orientiert sich am logischen Ablauf einer {{< termbase "Networked Audio">}}-Übertragung. Die besonderen Merkmale von Milan werden so erklärt, dass sie gut verständlich bleiben und der Lesefluss nicht gestört wird.

<!-- ## Milan terms -->
## Milan Fachbegriffe

<!-- Have a look at [Fig. 1](#fig-milan-names) which shows the general naming scheme in a Milan network. The terms are explained in the following. -->
Die Grafik in [Abb. 1](#fig-milan-names) zeigt, wie die Bezeichnungen in einem Milan-{{< termbase "Network">}} vergeben werden. Die einzelnen Begriffe werden im Folgenden erklärt.

<!-- {{< figure src="/images/milan-names.drawio.svg" alt="Milan Names" fig-num="1" title="Milan Names" id="fig-milan-names">}} -->
{{< figure src="/images/milan-names.drawio.svg" alt="Milan Names" fig-num="1" title="Milan Fachbegriffe" id="fig-milan-names">}}

<!-- ### Endstation -->
### {{< termbase "Endstation">}} {#endstation}

<!-- A device that converts audio from or into the Milan network. Endstations can contain either Talker or Listener functionality or contain both. Endstations are Milan certified. -->
Eine {{< termbase "Endstation">}} ist ein Gerät, das Audio in das Milan-Netzwerk einspeist oder daraus empfängt. Sie kann entweder die Funktion eines {{< termbase "Talker">}}, eines {{< termbase "Listener">}} oder beider Funktionen übernehmen. Alle {{< termbase "Endstations">}} sind Milan-zertifiziert.

<!-- ### Talker -->
#### {{< termbase "Talker">}}-Endstation {#talker-endstation}

<!-- A Talker converts an audio signal into the Milan network. Could be a digital microphone or a stage box. -->
Eine {{< termbase "Talker">}}-Endstation wandelt ein Audiosignal in das Milan-{{< termbase "Network">}} um. Beispiele dafür sind ein digitales Mikrofon oder eine Stagebox.

<!-- ### Listener -->
#### {{< termbase "Listener">}}-Endstation {#listener-endstation}

<!-- A Listener extracts an audio signal from the network. Could be an amplifier. -->
Eine {{< termbase "Listener">}}-Endstation entnimmt ein Audiosignal aus dem Milan-{{< termbase "Network">}}. Ein Beispiel dafür ist ein Verstärker.

<!-- ### Switch -->
### {{< termbase "Switch">}} {#Switch}

<!-- A Switch forwards streams from a Talker to a Listener. Usually, a Switch is the gPTP in a network. Switches are AVB certified. -->
Ein {{< termbase "Switch">}} leitet {{< termbase "Packets">}} zwischen verschiedenen {{< termbase "Ports">}} weiter. Meistens werden die Pakete von einem {{< termbase "Talker">}} zu einem {{< termbase "Listener">}} über die {{< termbase "Ports">}} des Switches übertragen. In der Regel übernimmt ein Switch dabei die Rolle des {{< tooltip "gPTP">}}-{{< termbase "Grandmaster">}} in einem {{< termbase "Network">}}. Alle Switches sind AVB-zertifiziert.

<!-- ### Bridged Endstation -->
### {{< termbase "Bridged Endstation">}} {#bridged-endstation}

<!-- A Bridged Endstation incorporates the Talker and or Listener functionality as well as the Switch functionality. -->
Eine {{< termbase "Bridged Endstation">}} vereint die Funktionen eines {{< termbase "Talker">}} und/oder {{< termbase "Listener">}} mit den Funktionen eines {{< termbase "Switch">}}.

<!-- ## OSI layers -->
## OSI Schichten

<!-- Milan operates on Open Systems Interconnection (OSI) layer 2. Meaning there is no need for IP addresses. All addressing in Milan is done via Medium Access Control (MAC) addresses. -->
Milan arbeitet auf der Open Systems Interconnection (OSI) {{< termbase "Data Link">}}s {{< termbase "Layer">}} ({{< termbase "Layer">}} 2). Das bedeutet, dass keine IP-Adressen benötigt werden. Die Adressierung erfolgt ausschließlich über {{< termbase "Media Access Control">}} (MAC)-Adressen.
