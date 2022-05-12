import optparse

def main():
    parser = optparse.OptionParser('usage %prog -H <host> -p <first-port> <last-port> -[f|s|x]')
    parser.add_option('-H', dest='host', type='string', help='specify target host')
    parser.add_option('-p', action='store',dest='ports')