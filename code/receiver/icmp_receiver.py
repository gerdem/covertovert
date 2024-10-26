import scapy.all as scapy

# Implement your ICMP receiver here

def packet_callback(packet):
    # Print the incoming ICMP packet
    print("Received packet:")
    packet.show()  # Display the packet details

if __name__ == "__main__":
    # Sniff for incoming ICMP packets
    scapy.sniff(filter="icmp", prn=packet_callback, store=0)
