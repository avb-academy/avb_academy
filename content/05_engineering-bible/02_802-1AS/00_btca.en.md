---
title: "Best TimeTransmitter Clock Algorithm"
date: 2026-04-02
weight: 1
---

In a network, configuring the Clock Leader does not require manual intervention. The {{< tooltip "gPTP">}} specification defines an algorithm that automatically selects the most suitable Clock Leader for the network.  

This mechanism is called the Best TimeTransmitter Clock Algorithm (BTCA), previously known as the Best Master Clock Algorithm (BMCA). The BTCA ensures that the network always operates under the most reliable and accurate time source available.

The election of a Clock Leader follows these rules:

- The election process stops if in any category a winner is determined.
- If two potential Clock Leaders have the same values in all categories, the final decision is made based on the MAC address of the device. The lower MAC address wins.

The election considers the following attributes, in order of priority:

1. [priority1](#priority1): Lower values are preferred and can influence which device becomes the Clock Leader.
2. [clockClass](#clockclass): Clocks are assigned a class reflecting their traceability to a primary time reference. Lower class numbers indicate higher reliability.
3. [clockAccuracy](#clockaccuracy): Clocks report their accuracy, and the algorithm favors clocks with higher accuracy (smaller deviation from the reference time).
4. [offsetScaledLogVariance](#offsetscaledlogvariance): The algorithm considers the clock's stability and precision. Smaller variances are preferred.
5. [MAC address](#mac-address): If all other parameters are equal, the clock with the lowest MAC address is selected.

### priority1

The priority1 field is the first considered attribute in the {{< tooltip "BTCA">}}. It describes the type of the system the clock sits in. The lower the quality, the better the clock.  The 802.1AS specification recommends three default values:

<!-- IEEE 802.1AS-2011, Table 8-2—Default values for priority1, for the respective media -->
| System type | Default priority1 value |
|-|-|
| Network infrastructure time-aware system | 246 |
| Other timer-aware systems | 248 |
| Portable time-aware system | 250 |
| Time-aware system that is not {{< tooltip "GM" >}} capable | 255 |

The priority1 value can be used to force a specific device to become the {{< tooltip "GM">}}. This is only recommended for special situations. Using the default values results in a stable system.

### clockClass

The clockClass tells you how reliable the time is that a device distributes when it acts as the {{< tooltip "GM" >}}. The value of the clockClass is based on how closely its time is tied to an official reference. An example for an official reference is GPS time.  
The clockClass is used by the {{< tooltip "BTCA">}} as part of the Grandmaster selection process. It is considered after [priority1](#priority1). Lower values are preferred.  
The values for the clockClass are

<!-- IEEE 1588-2008, Table 5 - clockClass specifications -->
| clockClass | Specification|
|-|-|
| 6 | Best possible clockClass. Locked to a primary reference like GPS or an atomic clock. Fully traceable to UTC. |
| 7 | A clock that was previously locked to a primary reference (class 6) but has lost it and is currently in holdover mode. |
| 52 | A clock that has lost its reference and no longer meets the requirements for holdover performance. |
| 187 | A clock that is not directly traceable to a primary reference and is synchronized via the network. |
| 248 | A free running clock that is not related to any primary reference. |
| 255 | A clock that is not suitable to become Grandmaster and is therefore excluded as a candidate in the BMCA. |

### clockAccuracy

The clockAccuracy parameter describes how closely the time of a ClockLeader matches a reference time. It represents the maximum expected deviation between the local clock and the reference.  
Lower values indicate higher accuracy. During the {{< tooltip "BTCA">}}, clocks with better accuracy are preferred.  
The specified accuracy windows range from 25ns to more than 10s:

<!-- IEEE1588-2008, Table 6 - clockAccuracy enumeration -->
| Value | Accuracy      | Value | Accuracy |
|-|-|-|-|
| 0x20  | within 25ns   | 0x29  | within 1ms    |
| 0x21  | within 100ns  | 0x2A  | within 2.5ms  |
| 0x22  | within 250ns  | 0x2B  | within 10ms   |
| 0x23  | within 1us    | 0x2C  | within 25ms   |
| 0x24  | within 2.5us  | 0x2D  | within 100ms  |
| 0x25  | within 10us   | 0x2E  | within 250ms  |
| 0x26  | within 25us   | 0x2F  | within 1s     |
| 0x27  | within 100us  | 0x30  | within 10s    |
| 0x28  | within 250us  | 0x31  | >10s          |

### offsetScaledLogVariance

The offsetScaledLogVariance is an estimate of the PTP variance. It describes the precision and frequency stability of the ClockMaster.  
For connaisseurs of formulas and deep math it is recommended to read through {{< global_reference ref="IEEE1588" clause="7.6.3" >}}. Everybody else can enjoy this summary in the meantime.


In short, the value tells you how stable the clock is: smaller numbers mean higher precision and stability, larger numbers mean lower precision.  

Technically, the variance is represented as follows:

1. Start with the variance of the clock in seconds squared.
2. Take the base-2 logarithm of this value.
3. Multiply the logarithm by {{< imath >}} 2^8 {{< /imath>}} to scale it.
4. Apply any hysteresis adjustments.
5. Represent the result as a 16-bit integer using two's complement, with 0x8000 added. Overflow is ignored.
6. The final number is called the offsetScaledLogVariance.

The value is either manufacturer-specified, measured online, or defaulted:

- Manufacturer-specified: The device may come with a known variance for its clock hardware (e.g., a GPS-disciplined oscillator). The manufacturer can predefine offsetScaledLogVariance based on that.  
- Measured online: If the device can measure its own clock stability in real time, it can compute the offsetScaledLogVariance from that measurement.  
- Fallback/default: If neither the manufacturer nor online measurement provides a value, the standard specifies 0x4100 as a safe default.


The smallest representable variance corresponds to an extremely stable clock, at about {{< imath >}} 3\cdot10^{-39}s^2 {{< /imath >}}. This gives an offsetScaledLogVariance of 0x0000.  

The largest representable variance corresponds to an extremely unstable or unknown clock, at about {{< imath >}} 2^{127.99609}s^2 {{< /imath >}}. This gives 0xFFFF.  

A value of 0xFFFF also indicates that the variance is too large to represent or has not been computed.

### MAC address

If all previously listed parameters are identical. The smallest MAC address is selected.