import socket
import sys

def get_service_by_ports(port=80, port_high=[]):
    """ Generate services by port #

    Args:
        port (int, optional): (Low Range of) Port to show service on. Defaults to 80.
        port_high (list, optional): High Range of Port to show service on. Defaults to [].

    Raises:
        ValueError: Invalid Port # (< 0 or > 65535)
    """
    if port < 0 or port > 65535:
        raise ValueError(f'Illegal port # {port}')

    if not port_high:
        port_high = port+1

    for p in range(port, port_high):
        try:
            serv = socket.getservbyport(p)
            print(f'Port {p}: {serv}')
        except OSError:
            continue

if __name__ == '__main__':
    """
    To try this program, use the following command:
    python service_by_ports.py min max
    min: Low address of port(s) to check
    max: [optional] High address of ports to check
    """
    try:
        max = int(sys.argv[2])
    except:
        max = []

    try:
        min = int(sys.argv[1])
    except:
        min = 213
    
    get_service_by_ports(min, max)