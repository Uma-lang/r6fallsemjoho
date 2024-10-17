# -*- coding: utf-8 -*-
import socket, os, binascii

host="127.0.0.1"

def main():
    socket_protocol = socket.IPPROTO_IP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        
    raw_buffer = sniffer.recvfrom(65565)[0]
    print(binascii.hexlify(raw_buffer).decode('utf-8'))
if __name__ == "__main__":
    main()