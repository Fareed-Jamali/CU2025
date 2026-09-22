# CU2025

## Concordia University IoT Devices Dataset

The **CU2025 Dataset** contains network traffic collected from IoT devices at Concordia University.

## Dataset Download

You can download the **CU2025 Dataset** using the link provided in [`CU2025_PCAP.txt`](CU2025_PCAP.txt).

## Combining PCAP Files

After downloading the ZIP file, you will find that the traffic for each device is distributed across multiple PCAP files.

To combine the PCAP files for a device into a single PCAP file, you can use the following script:

```bash
python combinecode.py
```
The script combines the individual PCAP files and generates a single output file named **merged_output**.

## Converting PCAP files to CSV

Once the PCAP files have been combined, you can convert the network traffic data from PCAP format to CSV format.

For this purpose, you can use:


```bash
python Scapy.py
```

Depending on your requirements, you may need to modify Scapy.py to extract additional features or customize the features included in the resulting CSV files.

## Adding Device Labels

If you would like to add labels corresponding to the IoT devices to the extracted data, you can use:

```bash
python label.py
```

This can be useful for machine learning and classification tasks where each network traffic record needs to be associated with its corresponding IoT device.

## Workflow

The recommended workflow is:

1. Download the dataset using the link provided in CU2025_PCAP.txt.

2. Extract the downloaded ZIP file.

3. Use combine code.py to combine multiple PCAP files into a single PCAP file for each device.

4. Use Scapy.py to convert the PCAP files into CSV files and extract the required network features.

5. Use label.py to add device labels if required.

## Files

| File                | Description   |
| -------------       | ------------- |
| ['CU2025_PCAP.txt'](CU2025_PCAP.txt)    | Contains the download link for the CU2025 Dataset  |
| ['combinecode.py'](combinecode.py)     | Combines multiple PCAP files into a single PCAP file  |
| ['Scapy.py'](Scapy.py)            | Converts PCAP files to CSV and extracts network traffic features  |
| ['Label.py'](Label.py)            | Adds labels corresponding to the IoT devices  |

## Note
* The feature extraction process in [`Scapy.py`](Scapy.py) can be customized depending on the requirements of your research or analysis.
* The labeling step is optional and can be performed if device-level labels are required.
* Make sure the required Python dependencies are installed before running the scripts.


