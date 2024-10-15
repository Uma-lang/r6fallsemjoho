# -*- coding: utf-8 -*-
import socket, os, binascii

host = "127.0.0.1"  # 必要に応じて自分のIPアドレスを指定

def main():
    socket_protocol = socket.IPPROTO_TCP  # MacOSではTCPを指定
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)[0]  # パケットを受信
            
            # IPヘッダー (最初の20バイト)
            ip_header = raw_buffer[0:20]
            protocol = ip_header[9]  # IPヘッダの9バイト目のプロトコル番号
            
            # IPヘッダのLengthを計算（ヘッダーの最初の4ビットがヘッダーの長さ）
            ip_header_length = (ip_header[0] & 0x0F) * 4

            if protocol == 6:  # TCPプロトコル
                tcp_header_start = ip_header_length  # TCPヘッダーはIPヘッダーの直後に始まる
                tcp_header = raw_buffer[tcp_header_start:tcp_header_start + 20]
                
                source_port = int.from_bytes(tcp_header[0:2], byteorder='big')  # 送信元ポート
                destination_port = int.from_bytes(tcp_header[2:4], byteorder='big')  # 宛先ポート
                
                # Destination Portが80 (HTTP) の場合のみ表示
                if destination_port == 80:
                    # TCP Offset (13バイト目の最初の4ビット)
                    tcp_header_length = (tcp_header[12] >> 4) * 4
                    payload_offset = tcp_header_start + tcp_header_length
                    
                    print(f"HTTP packet detected: Source Port: {source_port}, Destination Port: {destination_port}")
                    print(f"Payload starts at byte {payload_offset}")
                    print(binascii.hexlify(raw_buffer[payload_offset:]).decode('utf-8'))  # ペイロードの内容を16進数で表示

    except KeyboardInterrupt:
        pass  # プログラムが終了した際の例外処理

if __name__ == "__main__":
    main()