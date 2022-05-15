from threading import BoundedSemaphore
from socket import gethostbyname


class Scan():
    def __init__(self, first_port, last_port, host, timeout=0.250, max_connections=10):
        self.first_port = first_port
        self.last_port = last_port
        self.host = gethostbyname(host)
        self.timeout = timeout
        self.maxConnections = max_connections # Adjust this to change scanning speed
        self.connection_lock = BoundedSemaphore(self.maxConnections)
        self.open_ports = []
        if last_port is None:
            self.last_port = self.first_port # if the user only wants to scan one port

    def __str__(self):
        # ToString for all Scan objects
        string = ''
        for port in self.open_ports:
            string += f"[+] port {port} is open for business!\n"
        return string


