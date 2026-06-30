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

<!-- {{% notice info %}}
The Milan ecosystem is evolving rapidly. As a result, this list may not always reflect the latest available hardware. For the most up to date information, refer to the [Avnu Certified Product Registry](https://avnu.org/certified-product-registry/?cert=Milan).
{{% /notice %}} -->
{{% notice info %}}
Das Milan-Ökosystem entwickelt sich kontinuierlich weiter. Daher spiegelt diese Liste möglicherweise nicht immer den aktuellen Stand der verfügbaren Hardware wider. Die neuesten Informationen gibt es in der [Avnu Certified Product Registry](https://avnu.org/certified-product-registry/?cert=Milan).
{{% /notice %}}

<!-- ## Operating system independent -->
## Unabhängig vom Betriebssystem

<!-- The adapters listed in this section either use a manufacturer provided driver or implement a standardized interface such as USB Audio Class 2.0 (UAC2). As a result, they can be used on different operating systems without relying on an operating system specific Milan-AVB network stack. -->
Die in diesem Kapitel aufgelisteten Adapter verwenden entweder einen vom Hersteller bereitgestellten Treiber oder unterstützen standardisierte Schnittstellen wie die USB Audio Class 2.0 (UAC2). Dadurch können sie auf unterschiedlichen Betriebssystemen eingesetzt werden.

<!-- ### USB and Thunderbolt -->
### USB und Thunderbolt
- [Joyned MU16](https://joyned.io/products/mu16-usb-to-milan-interface)
- [MOTU 10pre](https://motu.com/en-us/products/10pre/)
- [MOTU 848](https://motu.com/en-us/products/848/)
- [MOTU 16A](https://motu.com/en-us/products/16a/)

<!-- ### PCIe -->
### PCIe
- [RME HDSPe AoX-M](https://rme-audio.de/hdspe-aox.html)

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
- [Sonnet Thunderbolt AVB Adapter](https://www.sonnettech.com/product/thunderbolt-avb-adapter/overview.html)
- [Sonnet Solo 10G](https://www.sonnettech.com/product/solo10g-tb3/overview.html)
- [OWC Thunderbolt 10G Adapter](https://www.owc.com/solutions/thunderbolt-3-10g-ethernet-adapter)
- [Kalea Informatique USB4 Thunderbolt 3 10G adapter](https://www.kalea-informatique.com/usb4-to-10g-ethernet-adapter.htm)
- [Sabrent USB4 to 10G adapter](https://sabrent.com/products/nt-p10g)

<!-- ## Windows systems -->
## Windows-Betriebssysteme

<!-- There is no known combination of available adapters.
Please refer to the [Milan certified product registry](https://avnu.org/certified-product-registry/?&cert=Milan) to find a Milan certified audio interface. -->
Derzeit sind keine bekannten Adapter für Milan-Netzwerke verfügbar.  
Bitte nutze die [Milan Certified Product Registry](https://avnu.org/certified-product-registry/?&cert=Milan), um ein Milan-zertifiziertes Audiointerface zu finden.

<!-- ## Linux systems -->
## Linux-Betriebssysteme

<!-- {{% notice info %}}
The adapters listed in the [Apple systems](#apple-systems) section are intended for use with macOS. For Linux systems, we therefore recommend only the adapters listed in this section.
{{% /notice %}} -->

{{% notice info %}}
Die im Abschnitt [Apple-Betriebssysteme](#apple-betriebssysteme) aufgelisteten Adapter sind für die Nutzung unter macOS vorgesehen. Für Linux-Systeme wird daher empfohlen, ausschließlich die in diesem Abschnitt genannten Adapter zu verwenden.
{{% /notice %}}


<!-- These Intel chipsets are known to support IEEE 802.1AS (gPTP) and 802.1Qav features, which are prerequisites for AVB functionality. Often, marketing refers to the gPTP support as IEEE 1588 support but pure IEEE 1588 support does not guarantee IEEE 802.1AS support. The use with a real-time kernel is recommended for best results. -->
Diese Intel-Chipsätze sind dafür bekannt, IEEE 802.1AS (gPTP) und 802.1Qav zu unterstützen. Beides grundlegende Voraussetzungen für AVB. Im Marketing wird häufig von IEEE 1588-Unterstützung gesprochen, jedoch garantiert reine IEEE 1588-Kompatibilität keine Unterstützung von IEEE 802.1AS. Für optimale Ergebnisse wird empfohlen, die Chipsätze zusammen mit einem Echtzeit-Kernel zu verwenden.

<!-- - [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html) -->
- [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html)
- [Sonnet Solo 10G](https://www.sonnettech.com/product/solo10g-tb3/overview.html)
