import socket
from scan import Scan
# TODO: rewrite in scapy so we can tell if the port is being filtered.

class FullConnect(Scan):
    def connect(self, port):
        # Takes in a (host, port) tuple
        try:
            s = socket.create_connection((self.host_resolved, port), self.timeout)
            s.close()
            self.open_ports.append(port)  # append ports to the port list
        # except statements are for errors relating to timeouts.
        except TimeoutError:
            pass
        except socket.timeout:
            pass
        except ConnectionRefusedError:
            pass
        finally:
            self.connection_lock.release()  # Release the thread
