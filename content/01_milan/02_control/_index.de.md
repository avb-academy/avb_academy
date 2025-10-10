---
title: "Steuerung"
date: 2025-02-11
weight: 3
---

<!-- {{% notice info %}}
- Control of Milan devices is specified in the AVB/TSN Discovery, Enumeration, Connection management, and Control protocol (ATDECC).
- Available controllers: [Milan Manager](https://milanmanager.com), [Nebra](https://meyersound.com/product/nebra/), [Hive](https://github.com/christophe-calmejane/Hive/releases)
{{% /notice %}} -->
{{% notice info %}}
- Die {{< termbase "Control">}} von Milan-Geräten erfolgt gemäß dem AVB/TSN Discovery, Enumeration, Connection management, and Control protocol (ATDECC).  
- Verfügbare {{< termbase "Controller">}} sind unter anderem: [Milan Manager](https://milanmanager.com), [Nebra](https://meyersound.com/product/nebra/), [Hive](https://github.com/christophe-calmejane/Hive/releases)
{{% /notice %}}

<!-- Milan AVB comes with a specification how to configure and monitor the devices. This is specified in the *AVB/TSN Discovery, Enumeration, Connection management, and Control* protocol (ATDECC). -->
Milan AVB enthält eine Spezifikation, wie Geräte konfiguriert und {{< termbase "Monitor">}} werden. Diese ist im *AVB/TSN Discovery, Enumeration, Connection management, and Control* Protocol (ATDECC) festgelegt.

<!-- The three main tasks are: -->
Das Protokoll erfüllt drei Hauptaufgaben:

<!-- - **Device Discovery**: It defines mechanisms for discovering devices on a network, ensuring that devices can be identified and enumerated efficiently.
- **Connection Management**: This includes establishing, managing, and tearing down connections between devices on the network.
- **Control Protocol**: This part of the standard specifies how devices can be controlled and configured. This includes managing device settings, handling configurations, and ensuring that devices operate correctly within the network. -->
- **{{< termbase "Device Discovery">}}**: Stellt sicher, dass Geräte im Netzwerk erkannt, zuverlässig identifiziert und enumeriert werden können.  
- **{{< termbase "Connection Management">}}**: Regelt Aufbau, Verwaltung und Abbau von Verbindungen zwischen Geräten im Netzwerk.  
- **{{< termbase "Control Protocol">}}**: Legt fest, wie Geräte gesteuert und konfiguriert werden. Dazu gehören die Verwaltung von Geräteeinstellungen und Konfigurationen sowie die Gewährleistung eines ordnungsgemäßen Betriebs innerhalb des Netzwerks.

<!-- ## Controllers -->
## {{< termbase "Controller">}}

<!-- There are currently a couple of solutions available: -->
Derzeit sind einige Lösungen verfügbar:

<!-- - Milan Manager: https://milanmanager.com/
- Nebra: https://meyersound.com/product/nebra/
- Hive: https://github.com/christophe-calmejane/Hive/releases -->
- Milan Manager: https://milanmanager.com/
- Nebra: https://meyersound.com/product/nebra/
- Hive: https://github.com/christophe-calmejane/Hive/releases
