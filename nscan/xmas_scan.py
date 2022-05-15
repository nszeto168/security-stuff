

# This is very similar to the syn scan.
#
def can_connect(ip_address, port, timeout_time = 0.200):
    source_port = random.randint(1, 65500) # random source port
    packet = scapy.all.IP(dst=ip_address) / scapy.all.TCP(sport=source_port, dport=port, flags="FPU") # make packet
    ans = scapy.all.sr1(packet, timeout=timeout_time, verbose=False) # send packet
    if ans == None: # if there was no response, return false
        return False
    else:
        return True

def scan(first_port,last_port, ip_address):
    #return [port for port in range (int(first_port), int(last_port) + 1 if can_connect(ip_address, port)]
    port_list = []
    for port in range (int(first_port), int(last_port)+1):
        if can_connect(ip_address, port):
            port_list.append(port)
    return port_list