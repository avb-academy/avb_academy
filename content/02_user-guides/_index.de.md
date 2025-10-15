---
title: "Milan Leitfäden"
date: 2025-02-11
weight: 4
---

{{% notice info %}}
- Milan Netzwerke benötigen time-aware Switches. Es wird empfohlen, Avnu-zertifizierte Switches zu verwenden. Andere TSN Switches werden höchstwahrscheinlich nicht per Plug-and-Play funktionieren. 
- AVB Switches benötigen keine QoS-Konfiguration wie es andere Audio over IP Protokolle erfordern.
- Die bevorzugte Netzwerk-Topologie ist immer sternförmig.
- Die Daumenregel für die maximale Anzahl an Hops lautet: 14 Hops für 1 Gbps Netzwerke und 7 Hops für 100 Mbps Netzwerke.
- Benutze qualitativ hochwertige CAT-Kabel.
- Redundanz wird im Milan Netzwerk durch zwei physisch separate Netzwerke erzeugt. Jedes Netzwerk benötigt einen eigenen gPTP GM. Unterschiedliche VLANs in einem Switch werden nicht funktionieren.
- Die Anzahl der Hops definiert die Ausspielverzögerung im Milan Netzwerk. Je geringer die Anzahl der Hops ist, desto geringer ist die Ausspielverzögerung.
{{% /notice %}}

<!-- More details can be found in the following sections: -->
Mehr Infos gibt es in den folgenden Abschnitten:
<!-- - [Certified Products](certified-products.md)
- [Getting started with Milan Manager](getting-started-milan-manager.md)
- [Network Adapters](network-adapters.md)
- [Number of hops](number-of-hops.md)
- [Redundancy](redundancy.md)
- [Switches](switches.md) -->
- [Zertifizierte Produkte](certified-products.md)
- [Erste Schritte mit dem Milan Manager](getting-started-milan-manager.md)
- [Netzwerk Adapter](network-adapters.md)
- [Anzahl Hops](number-of-hops.md)
- [Redundanz](redundancy.md)
- [Switches](switches.md)


