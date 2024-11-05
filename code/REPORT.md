# CENG 435 - Phase 1 Report

## Group 43

### Group Members

- Galip Erdem Çöl - 2521433

### GitHub

[Project Repository](https://github.com/gerdem/covertovert) 

### Procedure

- **Receiver Script**: The receiver listens incoming ICMP packets. Each time a packet is received, it triggers a callback function (packet_callback). It displays the packet details. After that, the receiver continues to listen indefinitely and whenever it captures a packet, it prints it to the console.
- **Sender Script**: The sender creates an ICMP packet with a destination IP (which is "receiver" in this case) and a TTL value of 1. Then, this packet is sent to the reciever using Scapy’s send function. After sending the packet, a message which confirms the packet has been sent, along with the destination IP, is printed to the console.
- **Sender-Receiver Interaction**: After running the sender script, an ICMP packet with TTL=1 is sent to the receiver container. The receiver, actively sniffing for ICMP packets, captures this packet. After that, it displays its contents in the terminal using the packet.show() method. This allows the receiver to display information about the packet structure, headers, and data.

