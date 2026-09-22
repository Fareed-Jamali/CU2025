import csv
from scapy.all import rdpcap, Ether, IP, TCP, UDP, DNS, ARP, ICMP
from scapy.layers.inet import IP, TCP, UDP
import socket

# Helper function to identify application protocols by port number
def get_app_protocol(port):
    if port == 80:
        return "HTTP"
    elif port == 443:
        return "HTTPS"
    elif port == 53:
        return "DNS"
    elif port == 25:
        return "SMTP"
    elif port == 110:
        return "POP3"
    elif port == 143:
        return "IMAP"
    else:
        return "Other"

def extract_features(pkt, last_pkt_time, packet_count, total_pkt_size, max_pkt_size, min_pkt_size, session_start_time):
    features = {}
    
    # Timestamp
    features['timestamp'] = pkt.time if hasattr(pkt, 'time') else 0
    features['time_diff'] = pkt.time - last_pkt_time if last_pkt_time is not None else 0

    # Ethernet layer
    if Ether in pkt:
        features['src_mac'] = pkt[Ether].src
        features['dst_mac'] = pkt[Ether].dst
    else:
        features['src_mac'] = 0
        features['dst_mac'] = 0
    
    # IP layer
    if IP in pkt:
        features['src_ip'] = pkt[IP].src
        features['dst_ip'] = pkt[IP].dst
        features['ip_len'] = len(pkt[IP])
        features['ttl'] = pkt[IP].ttl
        features['ip_proto'] = pkt[IP].proto
    else:
        features['src_ip'] = 0
        features['dst_ip'] = 0
        features['ip_len'] = 0
        features['ttl'] = 0
        features['ip_proto'] = 0
    
    # TCP layer
    if TCP in pkt:
        features['protocol'] = 'TCP'
        features['src_port'] = pkt[TCP].sport
        features['dst_port'] = pkt[TCP].dport
        features['flags'] = pkt[TCP].flags
        features['seq'] = pkt[TCP].seq
        features['ack'] = pkt[TCP].ack
        features['tcp_len'] = len(pkt[TCP])
        features['payload'] = len(pkt[TCP].payload)
        features['app_protocol'] = get_app_protocol(pkt[TCP].dport) if pkt[TCP].dport else "Other"
    # UDP layer
    elif UDP in pkt:
        features['protocol'] = 'UDP'
        features['src_port'] = pkt[UDP].sport
        features['dst_port'] = pkt[UDP].dport
        features['flags'] = 0
        features['seq'] = 0
        features['ack'] = 0
        features['udp_len'] = len(pkt[UDP])
        features['payload'] = len(pkt[UDP].payload)
        features['app_protocol'] = get_app_protocol(pkt[UDP].dport) if pkt[UDP].dport else "Other"
    else:
        features['protocol'] = 0
        features['src_port'] = 0
        features['dst_port'] = 0
        features['flags'] = 0
        features['seq'] = 0
        features['ack'] = 0
        features['payload'] = 0
        features['tcp_len'] = 0
        features['udp_len'] = 0
        features['app_protocol'] = "None"
    
    # ARP Layer (Address Resolution Protocol)
    if ARP in pkt:
        features['arp_op'] = pkt[ARP].op
        features['src_arp_mac'] = pkt[ARP].hwsrc
        features['dst_arp_mac'] = pkt[ARP].hwdst
        features['src_arp_ip'] = pkt[ARP].psrc
        features['dst_arp_ip'] = pkt[ARP].pdst
    else:
        features['arp_op'] = 0
        features['src_arp_mac'] = 0
        features['dst_arp_mac'] = 0
        features['src_arp_ip'] = 0
        features['dst_arp_ip'] = 0
    
    # ICMP Layer (Internet Control Message Protocol)
    if ICMP in pkt:
        features['icmp_type'] = pkt[ICMP].type
        features['icmp_code'] = pkt[ICMP].code
    else:
        features['icmp_type'] = 0
        features['icmp_code'] = 0
    
    # DNS Layer (if present)
    if DNS in pkt:
        features['dns_id'] = pkt[DNS].id
        features['dns_qr'] = pkt[DNS].qr
        features['dns_opcode'] = pkt[DNS].opcode
        features['dns_count'] = pkt[DNS].ancount
        features['dns_query_name'] = pkt[DNS].qd.qname.decode() if pkt[DNS].qd else 0
    else:
        features['dns_id'] = 0
        features['dns_qr'] = 0
        features['dns_opcode'] = 0
        features['dns_count'] = 0
        features['dns_query_name'] = 0
    
    # Length of the entire packet
    features['pkt_len'] = len(pkt)

    # Payload (raw data in the packet)
    features['raw_payload'] = len(pkt.payload)

    # Calculate Session Duration, Avg Packet Size, Max/Min Packet Size
    session_duration = pkt.time - session_start_time
    avg_pkt_size = total_pkt_size / packet_count if packet_count > 0 else 0
    features['session_duration'] = session_duration
    features['avg_pkt_size'] = avg_pkt_size
    features['max_pkt_size'] = max_pkt_size
    features['min_pkt_size'] = min_pkt_size

    return features

def pcap_to_csv(pcap_file, csv_file):
    packets = rdpcap(pcap_file)
    fieldnames = ['timestamp', 'time_diff', 'src_mac', 'dst_mac', 'src_ip', 'dst_ip', 'ip_len', 'ttl', 'ip_proto', 
                  'protocol', 'src_port', 'dst_port', 'flags', 'seq', 'ack', 'payload', 'pkt_len', 
                  'arp_op', 'src_arp_mac', 'dst_arp_mac', 'src_arp_ip', 'dst_arp_ip',
                  'icmp_type', 'icmp_code', 'dns_id', 'dns_qr', 'dns_opcode', 'dns_count', 'dns_query_name',
                  'raw_payload', 'udp_len', 'tcp_len', 'app_protocol', 'session_duration', 'avg_pkt_size', 
                  'max_pkt_size', 'min_pkt_size']  # Additional fields
    
    last_pkt_time = None
    packet_count = 0
    total_pkt_size = 0
    max_pkt_size = 0
    min_pkt_size = float('inf')
    session_start_time = None
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for pkt in packets:
            if session_start_time is None:  # Set session start time on first packet
                session_start_time = pkt.time
            
            # Update stats for session duration, avg/max/min packet size
            packet_count += 1
            total_pkt_size += len(pkt)
            max_pkt_size = max(max_pkt_size, len(pkt))
            min_pkt_size = min(min_pkt_size, len(pkt))

            features = extract_features(pkt, last_pkt_time, packet_count, total_pkt_size, max_pkt_size, min_pkt_size, session_start_time)
            writer.writerow(features)
            
            # Update last packet time for time difference
            last_pkt_time = pkt.time

# Example usage
pcap_file = "merged_output.pcap"  # Input pcap file
csv_file = "output48.csv"   # Output CSV file
pcap_to_csv(pcap_file, csv_file)
