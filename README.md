# CU2025

## Concordia University IoT Devices Dataset

The **CU2025 Dataset** contains network traffic collected from 27 IoT devices.

![System Architecture](CU2025_Dataset.png)

The list of the devices with their details follows.

| Sr.  | MAC Address | Device Name | Device Model | Device Instance |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | 08:12:A5:E0:5F:36  | Amazon Echo Dot (3rd Gen)  | C78MP8  | 1 of 1 |
| 2  | 18:7F:88:D4:C3:62  | Ring Battery Doorbell  | 5F97F2  | 1 of 1  |
| 3  | E8:4C:4A:B7:1B:DB  | Blink Video Doorbell  | BDM00200U  | 1 of 1  |
| 4  | DC:A0:D0:E1:AC:68  | Blink Outdoor Camera  | BCM00500U  | 1 of 1  |
| 5  | 68:13:F3:5E:E0:0A  | Blink Sync Module  | BSM00401U  | 1 of 1  |
| 6  | 5C:47:5E:90:26:06  | Chime Ring  | 5F67E9  | 1 of 1  |
| 7  | 1C:53:F9:CE:28:CD  | Google Nest Hub  | GUIK2  | 1 of 1  |
| 8  | 9C:C8:E9:82:95:31  | Amazon Echo Pop  | C2H4R9  | 1 of 1  |
| 9  | BC:DF:58:0A:CA:54  | Google Nest Mini (2nd Gen)  | H2C  | 1 of 1  |
| 10  | 60:74:F4:BB:B2:8E  | Goove Life Thermo-Hygrometer  | H5103  | 1 of 1  |
| 11  | C4:82:E1:25:0A:2A  | Rain Point WiFi Water Timer  | TWG004WRF  | 1 of 1  |
| 12  | AC:9F:C3:38:BF:58  | Ring StickUp Camera  | 5UM7E5  | 1 of 1  |
| 13  | EC:64:C9:E2:A7:84  | Smart Lock Gateway  | G2  | 1 of 1  |
| 14  | 2C:AA:8E:24:7C:59  | Wyze Camera Pan  | WYZECP1  | 1 of 1  |
| 15  | 50:13:95:B5:FC:20  | YI 1080p Home Camera  | YYS.2016  | 1 of 1  |
| 16  | A4:86:DB:5C:1F:D1  | Wifi Smart Camera  | T-CP8082LF-W3M  | 1 of 2  |
| 17  | A4:86:DB:59:B6:C2  | WiFi Smart Camera  | T-CP8082LF-W3M  | 2 of 2  |
| 18  | A4:86:DB:84:DB:4C  | WiFi Smart Camera  | T-CP8050LF-W3M  | 1 of 2  |
| 19  | A4:86:DB:84:DB:86  | WiFi Smart Camera  | T-CP8050LF-W3M  | 2 of 2  |
| 20  | 10:D5:61:05:AC:29  | Treat Life WiFi Smart Light  | SL20  | 1 of 2  |
| 21  | 10:D5:61:05:E8:04  | Treat Life WiFi Smart Light  | SL20  | 2 of 2  |
| 22  | 20:23:51:9A:C1:17  | Kasa Smart WiFi Plug  | HS103  | 1 of 2  |
| 23  | 20:23:51:9A:BE:7A  | Kasa Smart WiFi Plug  | HS103  | 2 of 2  |
| 24  | 9C:C8:E9:C2:89:76  | Camera Blink Mini 2  | BCM00700U  | 1 of 2  |
| 25  | 68:13:F3:1D:02:11  | Camera Blink Mini 2  | BCM00700U  | 2 of 2  |
| 26  | 3C:64:CF:BE:EC:C2  | Tapo Pan/Tilt Home Security WiFi Camera  | Tapo C210  | 1 of 2  |
| 27  | 3C:64:CF:BE:ED:F9  | Tapo Pan/Tilt Home Security WiFi Camera  | Tapo C210  | 2 of 2  |

## Dataset Download

You can download the **CU2025 Dataset** using the link provided in [`CU2025_PCAP.txt`](CU2025_PCAP.txt).

## Environment Creation

Once the dataset has been downloaded, you can create a virtual environment or use whatever environment setup works best for your workflow. The [`requirements.txt`](requirements.txt) file lists the dependencies required by another repository.

Please note that the original environment from which this code was obtained contained several additional dependencies and pieces of code that are not included in this repository. As a result, you may need to inspect the code and requirements.txt and install only the dependencies required to run the components you intend to use.

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

## Citation
Please cite the following in your reference.


<pre> Jamali, A.F., 2025. A Framework for Scalable Dataset Generation and Deep Learning-Based IoT Device Identification: Redefining the Future Paradigm (Masters dissertation, Concordia University).</pre>
