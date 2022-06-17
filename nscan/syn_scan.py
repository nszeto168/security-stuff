from scapy.layers.inet import IP, TCP, sr1
# scapy.all has some issues with pycharm so i used scapy.layers.inet
# REFERENCE: https://stackoverflow.com/questions/45691654/pycharm-unresolved-reference-with-scapy
import random
from scan import Scan


class Syn(Scan):
    def connect(self, port):
        source_port = random.randint(49152, 65500)  # ephemeral source port in compliance with RFC 6335
        packet = IP(dst=self.host_resolved) / TCP(sport=source_port, dport=port, flags="S")  # make packet
        ans = sr1(packet, timeout=self.timeout, verbose=False)  # send packet
        if ans is None:
            self.connection_lock.release()
            return
        ans.lastlayer()
        ans_flag = ans['TCP'].flags  # extract the tcp flag
        if ans_flag == 'SA':
            self.open_ports.append(port)
            reset = IP(dst=self.host_resolved) / TCP(sport=source_port, dport=port, flags="R")
            # Send a reset packet
            sr1(reset,timeout=self.timeout, verbose=False)
        elif ans_flag == 'R':
            # sometimes they will respond with reset
            self.open_ports.append(port)
        self.connection_lock.release()
