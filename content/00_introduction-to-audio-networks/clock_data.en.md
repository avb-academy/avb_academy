---
title: "Clock Data"
date: 2025-02-11
weight: 1
---

In a digital audio network, precise clocking is the basis for a functioning network. Components like analog-to-digital converters (ADC) and digital-to-analog converters (DAC) can not work properly without clocking. A networked audio device receives its clock signal from a master clock in the network. This can either be a dedicated device or a elected device that provides the master clock functionality among functionalities like processing audio. The networked audio device derives all necessary clock signals for its {{< tooltip "ADC">}} or {{< tooltip "DAC">}} from the master clock signal.

This master clock data keeps the system in sync, allowing everything to work smoothly. Transmitting clock data is the most important task to keep the audio network running correctly. Incorrect or missing clock data will lead to audio drop outs and system failures.

{{< figure src="/images/traffic-components-clock.drawio.svg" alt="Clocking" fig-num="1" title="Clock Data" id="fig-clock-data">}}