# -*- coding: utf-8 -*-
import socket, os, binascii

host = "127.0.0.1"

def main():
    socket_protocol = socket.IPPROTO_IP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)[0] # パケットを受信
            ip_header = raw_buffer[0:20] # IPヘッダーは最初の20バイト (IPv4の場合)
            protocol = ip_header[9] # プロトコルフィールドはIPヘッダーの9バイト目
            print(f"{protocol}") # プロトコル番号を表示
            if protocol == 1: # ICMPのプロトコル番号は1
                print(binascii.hexlify(raw_buffer).decode('utf-8')) # ICMPパケットの内容を16進数で表示
                
    except KeyboardInterrupt:
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    main()