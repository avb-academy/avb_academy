---
title: "Network Adapters"
date: 2020-05-19
weight: 60
---

{{% notice warning %}}
    This section presents adapters that should work with AVB Milan networks.

    **Please make sure before you buy that the adapter is working with your system.** 
{{% /notice %}}

Due to the [strict timing requirements](../01_milan/00_network-timing/_index.md) of Milan networks, specialized network adapters may be necessary. Different operating systems expose different interfaces, which may or may not support direct access to the network hardware.

## Apple systems 

These adapters are either natively supported by macOS or have proven reliable in AVB setups on Apple hardware.

- Thunderbolt 3 to Thunderbolt 2 Adapter
- [Sonnettech Thunderbolt AVB Adapter](https://www.sonnettech.com/product/thunderbolt-avb-adapter/overview.html)
- [OWC Thunderbolt 10G Adapter](https://www.owc.com/solutions/thunderbolt-3-10g-ethernet-adapter)

## Windows systems

There is no known combination of available adapters.
Please refer to the [Milan certified product registry](https://avnu.org/certified-product-registry/?&cert=Milan) to find a Milan certified audio interface.

## Linux systems

These Intel chipsets are known to support IEEE 1588 and 802.1Q features, which are prerequisites for AVB functionality. Use with a real-time kernel is recommended for best results.

- [Intel i210](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i210-controllers.html)
- [Intel i226](https://www.intel.de/content/www/de/de/products/details/ethernet/gigabit-controllers/i226-controllers/products.html)

