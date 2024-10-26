import scapy.all as scapy

# Implement your ICMP sender here

def create_icmp_packet(destination):
    # Create an ICMP packet with TTL=1
    packet = scapy.IP(dst=destination, ttl=1) / scapy.ICMP()
    return packet

def send_icmp_packet(packet):
    # Send the ICMP packet
    scapy.send(packet)

if __name__ == "__main__":
    destination_ip = "receiver"  # Use the hostname or IP of the receiver container
    icmp_packet = create_icmp_packet(destination_ip)
    send_icmp_packet(icmp_packet)
    print(f"ICMP packet sent to {destination_ip} with TTL=1")

