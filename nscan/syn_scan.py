# syn_scan.py
import scapy  # scapy bc its ez to syn scan with it
import socket


def make_packet(host, port):
    return scapy.sr1(scapy.IP(dst=host)/scapy.TCP(dport=port, flags="S"))


def send_packets(first_port,last_port, hostname): # this will send in a range
    for port in range(first_port, last_port):
        make_packet(socket.gethostbyname(hostname), port)


def send_select_packets(): # sends to ports in a select list
    return None

