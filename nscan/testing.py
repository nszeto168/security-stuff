import scapy.all
import random
source_port = random.randint(1,65500)
packet = scapy.all.IP( dst='8.8.8.8')/scapy.all.TCP(sport= source_port, dport=53, flags="S")
# reset =scapy.all.IP( dst='8.8.8.8')/scapy.all.TCP(sport=source_port, dport=[53, 52], flags="R")
ans = scapy.all.sr1(packet, timeout=0.2, verbose=False)

if ans == None:
    print("Port not closed!")
else:
    print("Port is open")