---
title: "Netzwerkadapter"
date: 2020-05-19
weight: 60
---

<!-- {{% notice warning %}}
This section presents adapters that should work with Milan AVB networks.

**Please make sure before you buy that the adapter is working with your system.** 
{{% /notice %}} -->
{{% notice warning %}}
Diese Seite beinhaltet Netzwerkadapter, die mit Milan-AVB-Netzwerken funktionieren sollten.  
**Bitte vor dem Kauf selbst sicherstellen, dass der Adapter mit deinem Computer kompatibel ist.**
{{% /notice %}}

<!-- Due to the [strict timing requirements](../01_milan/00_network-timing/_index.md) of Milan AVB networks, specialized network adapters may be necessary. Different operating systems expose different interfaces, which may or may not support direct access to the network hardware. -->
Aufgrund der sehr [strikten Anforderungen](../01_milan/00_network-timing/_index.md) an das Timing von Milan-AVB-Netzwerken können spezielle Netzwerkadapter erforderlich sein.  
Je nach Betriebssystem stehen unterschiedliche Schnittstellen zur Verfügung, die den direkten Zugriff auf die Hardware der Netzwerkkarte ermöglichen.

<!-- ## Apple systems  -->
## Apple-Betriebssysteme

<!-- These adapters are either natively supported by macOS or have proven reliable in AVB setups on Apple hardware. -->
Diese Adapter werden entweder nativ von macOS unterstützt oder haben sich in AVB-Setups auf Apple-Hardware als zuverlässig erwiesen:

<!-- - Thunderbolt 3 to Thunderbolt 2 Adapter
- Built-in network interfaces 
- [Sonnettech Thunderbolt AVB Adapter](https://www.sonnettech.com/product/thunderbolt-avb-adapter/overview.html)
- [OWC Thunderbolt 10G Adapter](https://www.owc.com/solutions/thunderbolt-3-10g-ethernet-adapter) -->

- Fest verbaute Netzwerkkarten
- Thunderbolt 3-zu-Thunderbolt 2-Adapter
- [Sonnettech Thunderbolt AVB Adapter](https://www.sonnettech.com/product/thunderbolt-avb-adapter/overview.html)
- [OWC Thunderbolt 10G Adapter](https://www.owc.com/solutions/thunderbolt-3-10g-ethernet-adapter)

<!-- ## Windows systems -->
## Windows-Betriebssysteme

<!-- There is no known combination of available adapters.
Please refer to the [Milan certified product registry](https://avnu.org/certified-product-registry/?&cert=Milan) to find a Milan certified audio interface. -->
Derzeit sind keine bekannten Adapter für Milan-Netzwerke verfügbar.  
Bitte nutze die [Milan Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Milan), um ein Milan-zertifiziertes Audiointerface zu finden.

<!-- ## Linux systems -->
## Linux-Betriebssysteme

<!-- These Intel chipsets are known to support IEEE 802.1AS (gPTP) and 802.1Qav features, which are prerequisites for AVB functionality. Often, marketing refers to the gPTP support as IEEE 1588 support but pure IEEE 1588 support does not guarantee IEEE 802.1AS support. The use with a real-time kernel is recommended for best results. -->
Diese Intel-Chipsätze sind dafür bekannt, IEEE 802.1AS (gPTP) und 802.1Qav zu unterstützen. Beides grundlegende Voraussetzungen für AVB. In Marketingmaterialien wird häufig von IEEE 1588-Unterstützung gesprochen, jedoch garantiert reine IEEE 1588-Kompatibilität keine Unterstützung von IEEE 802.1AS. Für optimale Ergebnisse wird empfohlen, die Chipsätze zusammen mit einem Echtzeit-Kernel zu verwenden.

<!-- - [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html) -->
- [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html)
