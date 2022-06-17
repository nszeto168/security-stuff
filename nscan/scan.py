from threading import BoundedSemaphore
from socket import gethostbyname
from threading import Thread
from time import sleep

class Scan():
    def __init__(self, port_range, host, timeout=0.250, max_connections=10):
        self.first_port = port_range[0]
        self.last_port = port_range[1]
        self.host_resolved = gethostbyname(host)
        self.host = host
        self.timeout = timeout
        self.maxConnections = max_connections # Adjust this to change scanning speed
        self.connection_lock = BoundedSemaphore(self.maxConnections)
        self.open_ports = []
        if self.last_port is None:
            self.last_port = self.first_port # if the user only wants to scan one port

    def __str__(self):
        # ToString for all Scan objects
        string = ''
        for port in self.open_ports:
            string += f"[+] port {port} is open\n"
        return string

    def connect(self, **kwargs):
        # Designed to be overwritten
        # This is here so we do not get any complaints from the run method
        return None

    def run(self):
        # Returns a list of open ports
        print(f"Scan for {self.host} ({self.host_resolved})")
        for port in range(int(self.first_port), int(self.last_port) + 1):
            self.connection_lock.acquire()  # Get a lock for a thread
            t = Thread(target=self.connect, args=[port])  # Select a port to scan
            # args has to be an iterable
            t.start()
        sleep(1)  # Allow time for the scans to catch up.
        return self.open_ports
