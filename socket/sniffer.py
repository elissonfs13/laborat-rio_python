import socket
import struct

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())
# create a raw socket and bind it to the public interface
s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))

s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    data = s.recvfrom(65565)
    packet = data[0]
    address = data[1]
    header = struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
    print(f'Adress: {address}')
    if header[6] == 6:  # header[6] is the field of the Protocol
        print("Protocol = TCP")
    elif header[6] == 1:
        print("Protocol = UDP")
    elif header[5] == 1:
        print("Protocol = ICMP")
