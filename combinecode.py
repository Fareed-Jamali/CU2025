import os
import subprocess

# Update this path to the folder containing your PCAP files
pcap_folder = 'C:/Users/User/Desktop/Dataset/NewDataset/Alexa_0812a5e05f36'

# If mergecap.exe is not in PATH, provide the full path here
mergecap_path = 'C:/Program Files/Wireshark/mergecap.exe'  # <-- adjust this if needed

# Show all files in the folder for debugging
print("\n Files in folder:")
for f in os.listdir(pcap_folder):
    print(" -", f)

# Gather all .pcap or .pcapng files (case-insensitive)
pcap_files = [f for f in os.listdir(pcap_folder) if f.lower().endswith('.pcap') or f.lower().endswith('.pcapng')]
pcap_full_paths = [os.path.join(pcap_folder, f).replace('\\', '/') for f in pcap_files]

# Function to get first packet timestamp using tshark
def get_first_timestamp(pcap_path):
    try:
        result = subprocess.check_output(
            ['tshark', '-r', pcap_path, '-T', 'fields', '-e', 'frame.time_epoch', '-c', '1'],
            stderr=subprocess.DEVNULL
        )
        return float(result.decode().strip())
    except Exception as e:
        print(f" Failed to read {pcap_path}: {e}")
        return float('inf')

# Map each file to its first packet timestamp
timestamped_files = [(get_first_timestamp(fp), fp) for fp in pcap_full_paths if os.path.exists(fp)]

# Sort the files by timestamp
timestamped_files.sort()
sorted_pcaps = [fp for _, fp in timestamped_files]

if not sorted_pcaps:
    print("\n No valid PCAP files found to merge.")
    exit(1)

# Prepare output path
output_file = os.path.join(pcap_folder, 'merged_output.pcap').replace('\\', '/')

# Build mergecap command with full path
merge_command = [mergecap_path, '-w', output_file] + sorted_pcaps

# Show merge order
print("\n Merging files in the following order:")
for file in sorted_pcaps:
    print("  -", file)

# Run mergecap
try:
    subprocess.run(merge_command, check=True)
    print(f"\n Merged PCAP created at: {output_file}")
except FileNotFoundError:
    print("\n 'mergecap' not found. Please install Wireshark CLI tools and update the path.")
except subprocess.CalledProcessError as e:
    print(f"\n Error while merging: {e}")
