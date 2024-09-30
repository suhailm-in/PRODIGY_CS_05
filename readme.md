# Network Packet Sniffer
## Overview
The Network Packet Sniffer is a Python tool designed to capture and analyze network packets in real-time. It provides essential information such as source and destination IP addresses, protocol types (TCP, UDP, ICMP), and the payload (data carried by the packets). This tool is useful for network monitoring, debugging, and cybersecurity analysis.

## Features
- Captures live network traffic on specified or default network interfaces.
- Displays source and destination IP addresses for each packet.
- Identifies protocol types (TCP, UDP, ICMP, and others).
- Extracts and shows packet payload data.
- Lightweight and customizable for additional features.

# Resources
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#Disclaimer)

## Requirements
To use this tool, ensure you have the following installed:
- Python 3.x
- Scapy library for packet sniffing and analysis.

### Installing Scapy
Use pip to install the scapy library:

```bash
pip install scapy
```

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/suhailm-in/PRODIGY_CS_05.git
```
```bash
cd PRODIGY_CS_05
```

## Usage
### Running the Packet Sniffer

1. Run the script with administrative/root privileges:
    ```bash
    sudo python packet_sniffer.py
    ```
    Note: Root/administrative privileges are required to capture network packets.


2. You can specify a network interface (e.g., eth0, wlan0) to monitor. If not specified, the default network interface will be used.

    ```bash
    sudo python packet_sniffer.py eth0
    ```

## How It Works

1. The script uses the `scapy` library's `sniff()` function to capture network packets.
2. A callback function (`packet_callback()`) processes each packet, extracting relevant information such as:
   - Source and Destination IP addresses.
   - Protocol type (e.g., TCP, UDP, ICMP).
   - Payload (the data being transmitted).
3. The output is displayed in real-time on the terminal as packets are captured.



## Disclaimer

This tool is for educational purposes and should only be used on networks where you have permission to monitor and analyze traffic. Unauthorized use may violate laws and result in legal consequences.



## Developed by
### Suhail M 
Ethical Hacker, Penetration Tester, and AI Researcher in Cybersecurity
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/suhailm_in" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="suhailm_online" height="30" width="40" /></a>
<a href="https://linkedin.com/in/suhailm-in" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="suhailm-online" height="30" width="40" /></a></p>















