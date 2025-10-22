---
title: "Redundanz"
date: 2025-02-11
weight: 50
---

<!-- Redundancy is an optional feature in Milan AVB. Therefore, not all Milan devices support redundancy. Non-redundant devices can still be connected to a redundant network, but without the failover capability.-->
Eine redundante Verbindung ist ein optionales Feature in Milan AVB. Deshalb unterstützen nicht alle Milan-Geräte Redundanz. Nicht-redundante Geräte können aber in ein redundantes Netzwerk eingebunden werden. Allerdings ohne die Ausfallsicherheit.

<!-- For a Milan network to be redundant, it must use physically separate networks. This means that the {{< tooltip "Primary">}} and {{< tooltip "Secondary">}} network each require their own dedicated {{< tooltip "Switch" "Switches">}}. Physical separation is necessary due to the way Milan operates. Specifically, each network must have its own {{< tooltip "gPTP">}} GrandMaster to maintain proper synchronization. The election of a {{< tooltip "gPTP">}} GrandMaster is described in [Network Synchronization :: Clock Leader Election](../01_milan/00_network-timing/#clock-leader-election). -->
Um ein Milan-Netzwerk redundant zu betreiben, muss es zwei physisch getrennte Netzwerke haben. Das bedeutet, dass das {{< tooltip "Primary">}}- und das {{< tooltip "Secondary">}}-Netzwerk jeweils eigene {{< tooltip "Switches" "Switch">}} benötigen. Die physische Trennung ist aufgrund der Funktionsweise von Milan notwendig. Insbesondere muss jedes Netzwerk seinen eigenen {{< tooltip "gPTP">}} GrandMaster besitzen, um eine korrekte Synchronisation zu gewährleisten. Die Wahl des {{< tooltip "gPTP">}} GrandMaster wird hier näher erläutert: [Network Synchronization :: Auswahl des Clock Leader im Netzwerk](../01_milan/00_network-timing/#auswahl-des-clock-leader-im-network).

<!-- Redundancy ensures that a pair of redundant ports ({{< tooltip "Primary">}} and {{< tooltip "Secondary">}}) continuously transmit the same audio data. As a result, both networks require identical bandwidth. In the event of a failure, seamless switching from one port to the other is possible without interruption of the audio signal. -->
Die Redundanz stellt sicher, dass ein redundantes Port-Paar ({{< tooltip "Primary">}} und {{< tooltip "Secondary">}}) kontinuierlich dieselben Audiodaten überträgt. Daher reservieren beide Netzwerke die gleiche Bandbreite. Fällt eines der beiden Netzwerke aus, erfolgt ein nahtloses Umschalten vom einen auf den anderen Port, ohne dass das Audiosignal unterbrochen wird.

<!-- This also means that you can not use one physical {{< tooltip "Switch">}} and separate the {{< tooltip "Primary">}} and {{< tooltip "Secondary">}} traffic with different VLANs like you could do this with other audio network protocols. -->
Das bedeutet auch, dass nicht ein einzelner physischer {{< tooltip "Switch">}} verwendet werden kann, um den {{< tooltip "Primary">}}- und {{< tooltip "Secondary">}}-Verkehr über unterschiedliche VLANs zu trennen, wie es bei anderen Audio-Netzwerkprotokollen möglich wäre.


<!-- {{< figure src="/images/redundancy.drawio.svg" alt="Redundancy scheme in Milan networks">}} -->
{{< figure src="/images/redundancy.drawio.svg" alt="Redundancy scheme in Milan networks">}}