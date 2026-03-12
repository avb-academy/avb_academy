---
title: "Basics"
date: 2026-03-12
weight: 4
---

## Ethernet Frame

The transmission of data is based on the Ethernet specification. An Ethernet frame with the relevant Layer 2 fields is shown in Table 3.

<table>
  <tr>
    <th colspan="6">Destination MAC</th>
    <th colspan="6">Source MAC</th>
    <th colspan="4">802.1Q tag</th>
    <th colspan="2">EtherType</th>
    <th colspan="5">Payload</th>
    <th colspan="4">CRC</th>
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
    <td colspan="2">TPID</td>
    <td colspan="2">PCP, DEI, VID</td>
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
    <td colspan="5"></td>
    <td colspan="4"></td>
  </tr>
</table>

### Destination MAC

Contains the MAC address of the destination of the frame. E.g. a {{< tooltip "Listener">}}.  
In this example the destination MAC address is 0x00-1D-C1-00-00-00.

### Source MAC

Contains the MAC address of the source of the frame. E.g. a {{< tooltip "Talker">}}.  
In this example, the source MAC address is 0x00-1B-C5-0A-C0-00.

### Q-tag

The Q-tag specifies the membership to a VLAN and the priority. Some readers might be familiar with that concept. At this point let us point out that {{< tooltip "SRP">}} and {{< tooltip "FQTSS">}} do take care of the configuration in the Switch.

#### Tag Protocol Identifier
The Tag Protocol Identifier (TPID) is set to a default value of 0x8100.  

#### Priority Code Point
The Priority Code Point (PCP) is used to indicate the membership of a Stream Reservation Class (SRClass). It is set to 2 for SRClass A Streams and set to 3 for SRClass B Streams.

#### Drop Eligible Indicator
The Drop Eligible Indicator (DEI) is used to indicate whether a frame is eligible to be dropped in the presence of congestion. Set to 0 (False).

#### Virtual LAN Identifier
The Virtual LAN Identifier (VID) is used to indicate membership for a high priority Stream. Milan traffic uses VID 2.

#### EtherType

The EtherType defines the traffic this frame belongs to. In Milan networks we have

| Protocol              | TPID    | EtherType | Defined in  |
|-                      |-        |-          |-            | 
| {{<tooltip "AVTP">}}  | 0x8100  | 0x22F0    | IEEE1722-2016, Table 5      |
| {{<tooltip "ATDECC">}}| -       | 0x22F0    | IEEE1722-2016, Table 5      |
| {{<tooltip "MAAP">}}  | -       | 0x22F0    | IEEE1722-2016, Table 5      |
| {{<tooltip "MSRP">}}  | -       | 0x22EA    | IEEE802.1Q-2011, Table 10-2 | 
| {{<tooltip "MVRP">}}  | -       | 0x88F5    | IEEE802.1Q-2011, Table 10-2 |
| {{<tooltip "MMRP">}}  | -       | 0x88F6    | IEEE802.1Q-2011, Table 10-2 |

As you can see, multiple protocol types use the same EtherType. The differentiation is then made with the subtypes. Please refer to the specific protocol subchapters.

#### Payload

The payload is depending on the data transmitted in the frame. It can be in the size of 42bytes to 1500bytes. Payloads smaller than 42bytes are zero-padded to the minimum size.

#### Cyclic Redundancy Check

The Cyclic Redundancy Check (CRC) is used to detect transmission errors and fix them.