import socket
from threading import Thread
from scan import Scan
from time import sleep


class FullConnect(Scan):
    def connect(self, host_port_pair):
        # Takes in a (host, port) tuple
        try:
            s = socket.create_connection(host_port_pair, self.timeout)
            s.close()
            host, port = host_port_pair
            self.open_ports.append(port)  # append ports to the port list
        except TimeoutError:
            pass
        except socket.timeout:
            pass
        finally:
            self.connection_lock.release()  # Release the thread

    def run(self):
        for port in range(int(self.first_port), int(self.last_port) + 2):
            self.connection_lock.acquire() # Get a lock for a thread
            t = Thread(target=self.connect, args=((self.host, port),))
            t.start()
            # self.connect((self.host, port))
        sleep(self.timeout)  # Allow time for the scans to catch up.
        return self.open_ports
