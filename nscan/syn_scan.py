import scapy.all
import random

def can_connect(ip_address, port, timeout_time = 0.200):
    source_port = random.randint(1, 65500) # random source port
    packet = scapy.all.IP(dst=ip_address) / scapy.all.TCP(sport=source_port, dport=port, flags="S") # make packet
    ans = scapy.all.sr1(packet, timeout=timeout_time, verbose=False) # send packet
    if ans == None: # if there was no response, return false
        return False
    else:
        return True


def scan(ip_address, first_port,last_port):
    # This sends a syn packet and returns false if there is no response
    #return [port for port in range (int(first_port), int(last_port) + 1 if can_connect(ip_address, port)]
    port_list = []
    for port in range (int(first_port), int(last_port)+1):
        if can_connect(ip_address, port):
            port_list.append(port)
    return port_list


print(scan("172.217.14.110", 80, 443))
