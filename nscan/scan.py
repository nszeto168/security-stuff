from threading import BoundedSemaphore


class Scan():
    def __init__(self, first_port, last_port, host, timeout=0.200, max_connections=10):
        self.first_port = first_port
        self.last_port = last_port
        self.host = host
        self.timeout = timeout
        self.maxConnections = max_connections # Adjust this to change scanning speed
        self.connection_lock = BoundedSemaphore(self.maxConnections)
        self.open_ports = []
