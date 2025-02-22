---
title: " AVB Academy"
---

# Introduction

You are looking for information about the Milan protocol, and someone mentioned that you can find it at the AVB Academy. However, you might be wondering: why AVB Academy when you are interested in Milan? Before answering that question, let us take a step back. What forms the foundation of Milan?

## Help Us Improve the AVB Academy

<div class="survey-notice">
  <p>AVB Academy is a passion project built in our spare time. To make it even better, we need your input! Your feedback will help us prioritize improvements and create content that truly benefits you.</p>
  <p>Take a minute to share your thoughts—your voice shapes the future of AVB Academy!</p>
  <div class="survey-button-container">
    {{% button href="https://forms.gle/wL78x5h2VFWfEmJ68" style="green" icon="circle-right"%}} Click here to take the survey{{% /button %}}
  </div>
</div>

<style>
  .survey-notice {
    background-color: #f9f9f9; /* Light background for light theme */
    color: #333; /* Dark text for light theme */
    padding: 20px;
    border-left: 5px solid #4CAF50; /* Green accent */
    margin-bottom: 20px;
    border-radius: 5px;
  }

  .survey-button-container {
    text-align: center;
    margin-top: 20px;
  }

  /* Dark theme adjustments */
  body.dark-theme .survey-notice {
    background-color: #333; /* Dark background for dark theme */
    color: #f9f9f9; /* Light text for dark theme */
    border-left: 5px solid #80e27e; /* Lighter green for better visibility */
  }

  body.dark-theme .survey-button-container {
    color: #f9f9f9; /* Light text for the button container */
  }

  .survey-notice {
  transition: background-color 0.3s ease, color 0.3s ease;
}

</style>



## Introduction to Time-Sensitive Networking (TSN)

Time-Sensitive Networking ({{< tooltip "TSN">}}) is a set of {{< tooltip "IEEE">}} standards that extend standard Ethernet to support real-time, deterministic communication. It enables guaranteed bandwidth, low latency, and synchronization for critical applications.

One of the first implementations of {{< tooltip "TSN">}} is {{< tooltip "AVB" >}}, designed for professional audio/video transport. {{< tooltip "AVB">}} provides features such as:

- Stream reservation for guaranteed bandwidth: [Details about Stream reservation](01_milan/03_traffic-shaping/stream-reservation/_index.md)
- Precise time synchronization using {{< tooltip "gPTP">}}: [Details about timing](01_milan/00_network-timing/_index.md)
- Low-latency forwarding with credit-based traffic shaping: [Details about traffic shaping](01_milan/03_traffic-shaping/fqtss/_index.md)

## Milan: The ProAV Flavor of AVB

{{< tooltip "Milan">}} is a ProAV-specific {{< tooltip "AVB">}} solution developed by the {{< tooltip "Avnu Alliance">}}. It ensures interoperability by defining a **deterministic** and **fully standardized** network transport layer for professional audio and video devices.

This knowledge base explores {{< tooltip "Milan">}} in detail, helping engineers and integrators understand its benefits and implementation.
