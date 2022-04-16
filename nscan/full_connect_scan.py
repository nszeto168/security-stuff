import socket


def can_connect(host_port_pair, timeout = 0.200):
    # Returns True when can connect. Returns False when it cannot connect
    try:
        socket.create_connection(host_port_pair, timeout)  # 200 ms timeout
        # makes the connection given a host and port
        # There has to be a way to continue sending traffic while waiting on other packets to timeout
        # right now it takes 3 min 20 sec to do a scan of 1000 ports
        return True
    except TimeoutError:
        return False


def scan(first_port, last_port, ip_address):
    port_list = [] # we will store the port numbers in here
    for port in range(int(first_port), int(last_port) +1 ):
        if can_connect((ip_address, port)):  # if you can connect add it to the list
            port_list.append(port)
    return port_list  # returns a list of ports


