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
```
The script combines the individual PCAP files and generates a single output file named **merged_output**.

## Converting PCAP files to CSV

Once the PCAP files have been combined, you can convert the network traffic data from PCAP format to CSV format.

For this purpose, you can use:


```bash
python "Scapy.py"
```

Depending on your requirements, you may need to modify Scapy.py to extract additional features or customize the features included in the resulting CSV files.

## Adding Device Labels

If you would like to add labels corresponding to the IoT devices to the extracted data, you can use:

```bash
python "label.py"
```

This can be useful for machine learning and classification tasks where each network traffic record needs to be associated with its corresponding IoT device.

## Workflow

The recommended workflow is:

Download the dataset using the link provided in CU2025_PCAP.txt.

Extract the downloaded ZIP file.

Use combine code.py to combine multiple PCAP files into a single PCAP file for each device.

Use Scapy.py to convert the PCAP files into CSV files and extract the required network features.

Use label.py to add device labels if required.
