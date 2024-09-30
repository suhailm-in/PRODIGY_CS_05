from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP


# Function to process captured packets
def packet_callback(packet):
    # Check if packet has IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine protocol type
        if protocol == 1:  # ICMP
            proto = "ICMP"
        elif protocol == 6:  # TCP
            proto = "TCP"
        elif protocol == 17:  # UDP
            proto = "UDP"
        else:
            proto = "Other"

        # Extract payload data if available
        payload = packet[IP].payload
        print(f"\n[+] Packet Captured:")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto}")
        print(f"Payload: {bytes(payload)}")


# Main function to start sniffing
def start_sniffer(interface=None):
    print("[*] Starting packet sniffer...")
    sniff(iface=interface, prn=packet_callback, store=False)


# Specify the network interface (e.g., eth0, wlan0) or leave as None for default
if __name__ == "__main__":
    start_sniffer(interface=None)
