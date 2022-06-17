import optparse  # parse options
from full_connect_scan import FullConnect
from syn_scan import Syn
from xmas_scan import Xmas
from find_range import findRange
parser = optparse.OptionParser('usage %prog <host> -p <first-port>-<last-port> -[f|s|x]')
parser.add_option('-p', dest='port_range', help='specify a range of ports or one port (default=1-1000)', default='1-1000')
parser.add_option('-t', dest='timeout', help='time in seconds that the host considers the target port unreachable (default=0.250)',
                  default='0.250')
parser.add_option('-T', dest='threads', help='specify maximum threads (connections) the program makes.'
                                             'More threads means more speed and less stealth. Less threads'
                                             'means less speed and more stealth (default=10)',
                  default='10')
parser.add_option('-f', action='store_true', dest='fc_scan', help='full connect flag', default=False)  # save as boolean
parser.add_option('-s', action='store_true', dest='s_scan', help='syn scan flag', default=False)
parser.add_option('-x', action='store_true', dest='x_scan', help='xmas scan flag', default=False)
options, args = parser.parse_args()

hosts = args # the hosts are taken in as args
port_range = findRange(options.port_range)
fc_scan = options.fc_scan
s_scan = options.s_scan
x_scan = options.x_scan
timeout = float(options.timeout)
threads = int(options.threads)
if fc_scan:
    for host in hosts:
        fc = FullConnect(port_range, host, timeout, threads)
        fc.run()
        print(fc)  # print the tostring
elif s_scan:
    for host in hosts:
        s = Syn(port_range, host, timeout, threads)
        s.run()
        print(s)  # print the tostring
elif x_scan:
    for host in hosts:
        x = Xmas(port_range, host, timeout, threads)
        x.run()
        print(x)

