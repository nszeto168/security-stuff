import optparse  # parse options
from full_connect_scan import FullConnect
# TODO: User parser to take in hosts as args
parser = optparse.OptionParser('usage %prog <host> -p <first-port> -P <last-port> -[f|s|x]')
parser.add_option('-p', dest='first_port', help='specify first port (default=1)', default=1)
parser.add_option('-P', dest='last_port', help='specify last port (default=1000)', default=1000)
parser.add_option('-t', dest='timeout', help='time in seconds that the host considers the target port unreachable (default=0.250)',
                  default='0.250')
parser.add_option('-T', dest='threads', help='specify maximum threads (connections) the program makes'
                                             'more threads means more speed and less stealth. Less threads'
                                             'means less speed and more stealth (default=10)',
                  default='10')
parser.add_option('-f', action='store_true', dest='fc_scan', help='full connect flag', default=False)  # save as boolean
parser.add_option('-s', dest='syn_scan', help='syn scan flag')
options, args = parser.parse_args()

hosts = args # the hosts are taken in as args
first_port = options.first_port
last_port = options.last_port
fc_scan = options.fc_scan
timeout = float(options.timeout)
threads = int(options.threads)
if fc_scan:
    for host in hosts:
        fc = FullConnect(first_port, last_port, host, timeout, threads)
        fc.run()
        print(f"Scan for {host}")
        print(fc) # print the tostring
