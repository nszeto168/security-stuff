import scapy.all

packet = scapy.all.IP(dst='8.8.8.8')/scapy.all.TCP(dport=[53, 52])
ans, unans = scapy.all.sr(packet)

print(ans)
#print(unans)