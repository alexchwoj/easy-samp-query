import socket

def encode_bytes(*args):
    result = b''
    for arg in args:
        if isinstance(arg, bytes):
            result += arg
        elif isinstance(arg, str):
            result += bytes(arg)
        elif isinstance(arg, int):
            result += bytes([arg])
    return result

def send_query(ip_address, port = 7777, opcode = 'i', timeout = 3):
    """Send query packet to server"""
    ip_address = socket.gethostbyname(ip_address)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    
    sock.sendto(
        b'SAMP' \
        + encode_bytes(*[(int(n)) for n in ip_address.split('.')]) \
        + encode_bytes(int(port) & 0xFF, int(port) >> 8 & 0xFF) \
        + opcode.encode() \
        + b'',
        (ip_address, port)
    )

    data = sock.recv(4096)
    sock.close()
    
    return data[11:]