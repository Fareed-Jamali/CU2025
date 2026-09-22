# CU2025

## Concordia University IoT Devices Dataset

The **CU2025 Dataset** contains network traffic collected from IoT devices at Concordia University.

## Dataset Download

You can download the **CU2025 Dataset** using the link provided in [`CU2025_PCAP.txt`](CU2025_PCAP.txt).

## Combining PCAP Files

After downloading the ZIP file, you will find that the traffic for each device is distributed across multiple PCAP files.

To combine the PCAP files for a device into a single PCAP file, you can use the following script:

```bash
python "combine code.py"
combine code.py	Combines multiple PCAP files into a single PCAP file
Scapy.py	Converts PCAP files to CSV and extracts network traffic features
label.py	Adds labels corresponding to the IoT devices
Notes

The feature extraction process in Scapy.py can be customized depending on the requirements of your research or analysis.

The labeling step is optional and can be performed if device-level labels are required.

Make sure the required Python dependencies are installed before running the scripts.
Use label.py to add device labels if required.

Files
File	Description
CU2025_PCAP.txt	Contains the download link for the CU2025 Dataset
combine code.py	Combines multiple PCAP files into a single PCAP file
Scapy.py	Converts PCAP files to CSV and extracts network traffic features
label.py	Adds labels corresponding to the IoT devices
