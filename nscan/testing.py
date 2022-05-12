import optparse

parser = optparse.OptionParser('stuff here')
parser.add_option('-p', action='store', dest='port_tuple')
options = parser.parse_args()


# print(f"arguments: {options.port_tuple}")
print(f"options: {options}")