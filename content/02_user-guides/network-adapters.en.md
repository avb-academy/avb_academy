---
title: "Network Adapters"
date: 2020-05-19
weight: 60
---

{{% notice warning %}}
This section presents adapters that should work with Milan AVB networks.  
**Please make sure before you buy that the adapter is working with your system.** 
{{% /notice %}}

Due to the [strict timing requirements](../01_milan/00_network-timing/_index.md) of Milan AVB networks, specialized network adapters may be necessary. Different operating systems expose different interfaces, which may or may not support direct access to the network hardware.

{{% notice info %}}
The Milan ecosystem is evolving rapidly. As a result, this list may not always reflect the latest available hardware. For the most up to date information, refer to the [Avnu Certified Product Registry](https://avnu.org/certified-product-registry/?cert=Milan).
{{% /notice %}}

## Operating system independent

The adapters listed in this section either use a manufacturer provided driver or implement a standardized interface such as USB Audio Class 2.0 (UAC2). As a result, they can be used on different operating systems.

### USB and Thunderbolt
- [Joyned MU16](https://joyned.io/products/mu16-usb-to-milan-interface)
- [MOTU 10pre](https://motu.com/en-us/products/10pre/)
- [MOTU 848](https://motu.com/en-us/products/848/)
- [MOTU 16A](https://motu.com/en-us/products/16a/)

### PCIe
- [RME HDSPe AoX-M](https://rme-audio.de/hdspe-aox.html)

## Apple systems 

These adapters are either natively supported by macOS or have proven reliable when used with AVB networks on Apple hardware.

- Built-in network interfaces 
- Apple Thunderbolt 3 to Thunderbolt 2 Adapter
- [Sonnet Thunderbolt AVB Adapter](https://www.sonnettech.com/product/thunderbolt-avb-adapter/overview.html)
- [Sonnet Solo 10G](https://www.sonnettech.com/product/solo10g-tb3/overview.html)
- [OWC Thunderbolt 10G Adapter](https://www.owc.com/solutions/thunderbolt-3-10g-ethernet-adapter)
- [Kalea Informatique USB4 Thunderbolt 3 10G adapter](https://www.kalea-informatique.com/usb4-to-10g-ethernet-adapter.htm)
- [Sabrent USB4 to 10G adapter](https://sabrent.com/products/nt-p10g)

## Windows systems

There is no known combination of available adapters.
Please refer to the [Milan certified product registry](https://avnu.org/certified-product-registry/?&cert=Milan) to find a Milan certified audio interface.

## Linux systems

{{% notice info %}}
The adapters listed in the [Apple systems](#apple-systems) section are intended for use with macOS. For Linux systems, we therefore recommend only the adapters listed in this section.
{{% /notice %}}

The following network adapters are based on chipsets that are known to support IEEE 802.1AS (gPTP) and IEEE 802.1Qav, which are prerequisites for AVB functionality. Some manufacturers advertise IEEE 802.1AS support as IEEE 1588 support. However, IEEE 1588 support alone does not guarantee compatibility with IEEE 802.1AS. For the best results, using a real time kernel is recommended.

- [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html)
- [Sonnet Solo 10G](https://www.sonnettech.com/product/solo10g-tb3/overview.html)



