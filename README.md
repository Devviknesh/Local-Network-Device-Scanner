# Local-Network-Device-Scanner
Finds devices connected to the same WiFi network.

Local Network Device Scanner

Overview

The Local Network Device Scanner is a lightweight tool that scans the local network for connected devices, displaying their IP addresses, MAC addresses, and manufacturer details. This project is useful for network administrators, security enthusiasts, and developers looking to analyze network activity.

Features

Scans the local network for active devices

Displays IP and MAC addresses of connected devices

Identifies device manufacturers using MAC vendor lookup

Lightweight and easy to use

Technologies Used

Python

scapy for network packet analysis

argparse for command-line arguments

requests for MAC vendor lookup (optional)

Installation

Clone the repository:

git clone https://github.com/your-username/local-network-scanner.git
cd local-network-scanner

Install dependencies:

pip install scapy requests

Usage

Run the script with administrator privileges:

python scanner.py

You can also specify an IP range to scan:

python scanner.py --ip-range 192.168.1.0/24

Example Output

Scanning network...
-----------------------------------
IP Address     MAC Address       Manufacturer
192.168.1.1    00:1A:2B:3C:4D:5E  Cisco Systems
192.168.1.5    11:22:33:44:55:66  Dell Inc.
-----------------------------------
Scan complete.

Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
