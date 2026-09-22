# CU2025

## Concordia University IoT Devices Dataset

The **CU2025 Dataset** contains network traffic collected from IoT devices at Concordia University.

## Dataset Download

You can download the **CU2025 Dataset** using the link provided in [`CU2025_PCAP.txt`](CU2025_PCAP.txt).

## Combining PCAP Files

After downloading the ZIP file, you will find that the traffic for each device is distributed across multiple PCAP files.

To combine the PCAP files for a device into a single PCAP file, you can use the following script:

```bash
python "combinecode.py"
