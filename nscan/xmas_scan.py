from scapy.layers.inet import IP, TCP, sr1
import random
from scan import Scan
#f This is very similar to the syn scan in fact I basically copy+pasted it all


class Xmas(Scan):
    def connect(self, port):
        source_port = random.randint(49152, 65500)  # ephemeral source port in compliance with RFC 6335
        packet = IP(dst=self.host_resolved) / TCP(sport=source_port, dport=port, flags="FPU")  # make packet
        ans = sr1(packet, timeout=self.timeout, verbose=False)  # send packet
        if ans is None:
            # stop if there is no answer
            self.connection_lock.release()  # Release the thread
            return
        ans.lastlayer()
        ans_flag = ans['TCP'].flags  # extract the tcp flag
        if ans_flag == 'R' or 'RA':
            pass
        else:
            self.open_ports.append(port)
        self.connection_lock.release()  # Release the thread
