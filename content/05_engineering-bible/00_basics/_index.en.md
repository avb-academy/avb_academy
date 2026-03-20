---
title: "Basics"
date: 2026-03-12
weight: 4
---

{{% notice info %}}
- MAC addresses operate on OSI layer 2 and are used for local delivery within an Ethernet network
- IP addresses operate on OSI layer 3 and enable communication across different networks
- Milan-AVB Streams are utilizing multicast MAC addresses to forward Streams efficiently
- Bandwidth for Milan-AVB Streams is reserved dynamically using SRP.
{{%/notice%}}

## MAC Addressing vs. IP Addressing

TODO: Link OSI Layer section

Milan-AVB uses {{< tooltip "MAC">}} addresses to communicate. As described in the [OSI layer section](todo-link), the MAC address is part of layer 2. Therefore, it is used by all higher layer protocols that rely on Ethernet. This means that even if communication is based on {{< tooltip "IP">}} addresses, the data is ultimately transmitted using MAC addresses on the physical network.

In Milan-AVB systems, the control and media transport protocols operate directly on layer 2 without requiring IP addressing. This reduces complexity and avoids the need for IP configuration.

IP addresses belong to layer 3 and are used for logical addressing and routing between networks. In contrast, MAC addresses are used for communication within a local network segment. When a device wants to send data to an IP address, it must first determine the corresponding MAC address. This mapping is typically performed using the Address Resolution Protocol ({{< tooltip "ARP">}}).

MAC addresses are 48 bits long and are typically written as six groups of hexadecimal values. The first part identifies the manufacturer ({{< tooltip "OUI">}}), while the second part is assigned by the manufacturer to uniquely identify the device.  
An exemplary MAC address could be: `3C:C0:C6:00:AA:BB`. The following table distinguishes between the Organizationally Unique Identifier (OUI) and the unique part identifying the device. Feel free to look up the organization to which this MAC address belongs to here: [https://oui.is](https://oui.is).

<table>
  <tr>
    <th colspan="1"> OUID </th>
    <th colspan="1"> Unique part </th>
  </tr>
  <tr>
    <td>3C:C0:C6</td>
    <td>00:AA:BB</td>
  </tr>
</table>

The neat thing about MAC addresses is that they are assigned to the hardware of the Ethernet interface by the manufacturer and are intended to be globally unique. This reduces the risk of configuration errors compared to IP addresses, which must be assigned and managed by the user or network administrator.

MAC addresses can represent different types of destinations. A unicast MAC address identifies a single device, while a multicast MAC address identifies a group of devices. This distinction is encoded directly in the MAC address itself.

This is particularly important in Milan-AVB, where multicast MAC addresses are used to distribute Streams to multiple Listeners.

Section [Ethernet Frame](#ethernet-frame) gives you an impression what exactly might be contained in an Ethernet frame that is used in Milan-AVB.

## Unicast vs. Multicast Traffic

All {{< tooltip "Streams" "Stream">}} in Milan-AVB are multicast streams. Instead of sending data to a single receiver, a {{< tooltip "Talker">}} transmits a stream to a multicast {{< tooltip "MAC">}} address. This allows multiple {{< tooltip "Listeners" "Listener">}} to receive the same stream simultaneously.

Compared to unicast traffic, where a separate data stream must be sent to each receiver, multicast uses bandwidth more efficiently. The stream is transmitted only once by the Talker, and the switches ensure that it is forwarded only to the ports where interested Listeners are connected.

In a Milan-AVB network, this forwarding behavior is controlled dynamically. {{< tooltip "SRP">}} is used by Listeners to register their interest in a stream. Based on this information, switches build forwarding tables and reserve the required bandwidth along the path between Talker and Listeners.  
This mechanism ensures efficient use of bandwidth and automatic configuration of the network without manual intervention. It also guarantees that bandwidth is only reserved if at least one Listener is present.

In contrast, unicast traffic is typically used for point-to-point communication, such as control data or configuration messages, where only a single receiver is involved.

## Ethernet Frame

An Ethernet frame with the relevant layer 2 fields is shown in Table 3.

Before looking into the individual fields, it is important to understand that the Ethernet frame defines how data is structured on the wire. Each field has a fixed position and size, allowing all devices in the network to interpret the frame correctly.  
Note that the Ethernet frame shown here focuses on the layer 2 payload structure. Lower-level fields such as the preamble and start frame delimiter (SFD), which are used for synchronization on the physical layer, are omitted for clarity.
<table>
  <tr>
    <th colspan="6"><a href=#destination-mac>Destination MAC</a></th>
    <th colspan="6"><a href=#source-mac>Source MAC</a></th>
    <th colspan="4"><a href=#q-tag>Q tag</a></th>
    <th colspan="2"><a href=#ethertype>EtherType</a></th>
    <th colspan="5"><a href=#payload>Payload</a></th>
    <th colspan="4"><a href=#cyclic-redundancy-check>CRC</a></th>
  </tr>
  <tr>
    <td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
    <td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
    <td>1</td><td>2</td><td>3</td>
    <td>4</td>
    <td>1</td><td>2</td>
    <td>1</td><td>2</td><td>3</td><td>...</td><td>n</td>
    <td>1</td><td>2</td><td>3</td><td>4</td>
  </tr>
  <tr>
    <td colspan="6"></td>
    <td colspan="6"></td>
    <td colspan="2"><a href=#tag-protocol-identifier>TPID</a></td>
    <td colspan="2"><a href=#priority-code-point>PCP</a>, <a href=#drop-eligible-indicator>DEI</a>, <a href=#virtual-lan-identifier>VID</a></td>
    <td colspan="2"></td>
    <td colspan="5">n = 42 to 1500</td>
    <td colspan="4"></td>
  </tr>
  <tr>
    <td>00</td><td>1D</td><td>C1</td><td>00</td><td>00</td><td>00</td>
    <td>00</td><td>1B</td><td>C5</td><td>0A</td><td>C0</td><td>00</td>
    <td>81</td><td>00</td>
    <td>60</td><td>02</td>
    <td>22</td><td>F0</td>
    <td>XX</td><td>XX</td><td>XX</td><td>XX</td><td>XX</td>
    <td></td><td></td><td></td><td></td>
  </tr>
</table>

In Milan-AVB networks, Ethernet frames are used to transport both control information and time-sensitive media streams. The correct interpretation of these fields is essential for interoperability between devices.

### Destination MAC

Contains the MAC address of the destination of the frame. This can either be a unicast address (single device) or a multicast address (multiple devices), which is commonly used in Milan for stream distribution. E.g. a {{< tooltip "Listener">}}.  
In this example the destination MAC address is `00:1D:C1:00:00:00`.

### Source MAC

Contains the MAC address of the source of the frame. E.g. a {{< tooltip "Talker">}}.  
In this example, the source MAC address is `00:1B:C5:0A:C0:00`.

### Q-tag

The Q-tag specifies the membership to a {{< tooltip "VLAN">}} and the priority. It enables traffic separation and prioritization, which is essential for deterministic audio transport. Some readers might be familiar with that concept. At this point let us point out that {{< tooltip "SRP">}} and {{< tooltip "FQTSS">}} are used to configure traffic reservation and transmission behavior in the switch

#### Tag Protocol Identifier
The Tag Protocol Identifier (TPID) is set to a default value of `0x8100` and indicates that a {{< tooltip "VLAN">}} tag is present.

#### Priority Code Point
The Priority Code Point (PCP) is used to indicate the membership of a Stream Reservation Class (SRClass).
The PCP value is set to `2` for SRClassA and to `3` for SRClassB.

#### Drop Eligible Indicator
The Drop Eligible Indicator (DEI) is used to indicate whether a frame is eligible to be dropped in the presence of congestion. It is set to 0 (false) for Milan-AVB traffic.

#### Virtual LAN Identifier
The Virtual LAN Identifier (VID) is used to indicate membership for a high priority Stream. Milan traffic uses VID `2`.

#### EtherType

The EtherType defines the traffic this frame belongs to. In Milan networks we have

| Protocol              | TPID    | EtherType | Defined in  |
|-                      |-        |-          |-            | 
| {{<tooltip "AVTP">}}  | 0x8100  | 0x22F0    | {{< global_reference ref="IEEE1722">}}, Table 5      |
| {{<tooltip "ATDECC">}}| -       | 0x22F0    | {{< global_reference ref="IEEE1722">}}, Table 5      |
| {{<tooltip "MAAP">}}  | -       | 0x22F0    | {{< global_reference ref="IEEE1722">}}, Table 5      |
| {{<tooltip "MSRP">}}  | -       | 0x22EA    | {{< global_reference ref="IEEE8021Q">}}, Table 10-2 | 
| {{<tooltip "MVRP">}}  | -       | 0x88F5    | {{< global_reference ref="IEEE8021Q">}}, Table 10-2 |
| {{<tooltip "MMRP">}}  | -       | 0x88F6    | {{< global_reference ref="IEEE8021Q">}}, Table 10-2 |

As you can see, multiple protocol types use the same EtherType. The differentiation is then made using protocol-specific subtype fields within the payload and is described in the respective protocol sections.

#### Payload

The payload contains the actual protocol data being transmitted, such as audio samples, control messages, or reservation information. It can have a size of 42 bytes to 1500 bytes. Payloads smaller than the minimum size are padded with zeros.

#### Cyclic Redundancy Check

The Cyclic Redundancy Check (CRC) is used to detect transmission errors. Frames with invalid CRC values are discarded by receiving devices.