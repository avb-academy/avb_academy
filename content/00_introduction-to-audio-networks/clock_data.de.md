---
title: "Synchronisationsdaten"
date: 2025-02-11
weight: 1
---

<!-- Original English Comment -->
<!-- In a digital audio network, precise clocking is the basis for a functioning network. Components like analog-to-digital converters (ADC) and digital-to-analog converters (DAC) can not work properly without clocking. A networked audio device receives its clock signal from a master clock in the network. This can either be a dedicated device or a elected device that provides the master clock functionality among functionalities like processing audio. The networked audio device derives all necessary clock signals for its ADC or DAC from the master clock signal. -->
In einem Audionetzwerk ist eine präzise Taktung die Grundlage für ein funktionierendes Netzwerk. Bauteile wie {{< termbase "Analog To Digital Converters">}} (ADC) und {{< termbase "Digital To Analog Converters">}} (DAC) können ohne korrekte Taktung nicht richtig arbeiten. Ein {{< termbase "Networked Audio">}}-Gerät empfängt seinen Takt von einer {{< termbase "Master Clock">}} im {{< termbase "Network">}}. Dies kann entweder ein bestimmtes Gerät für genau diesen Zweck sein oder ein Gerät, das die {{< termbase "Master Clock">}}-Funktion übernimmt. Das {{< termbase "Networked Audio">}}-Gerät leitet die benötigten {{< termbase "Clocks">}} für {{< tooltip "ADC">}} und {{< tooltip "DAC">}} vom {{< termbase "Master Clock">}}-Signal ab.

<!-- Original English Comment -->
<!-- This master clock data keeps the system in sync, allowing everything to work smoothly. Transmitting clock data is the most important task to keep the audio network running correctly. Incorrect or missing clock data will lead to audio drop outs and system failures. -->
Diese {{< termbase "Master Clock">}} stellt sicher, dass das gesamte {{< termbase "Network">}} synchronisiert ist und alle Komponenten reibungslos zusammenarbeiten. Die Übertragung der {{< termbase "Clock">}}-Signale ist eine der wichtigsten Aufgaben in einem Audionetzwerk. Ohne korrekte {{< termbase "Clock">}}-Signale kann es zu Übertragungsfehlern und bis hin zu Systemausfällen kommen.

<!-- {{< figure src="/images/traffic-components-clock.drawio.svg" alt="Clocking" fig-num="1" title="Clock Data" id="fig-clock-data">}} -->
{{< figure src="/images/traffic-components-clock.drawio.svg" alt="Clock Signals" fig-num="1" title="Synchronisationsdaten" id="fig-clock-data">}}
