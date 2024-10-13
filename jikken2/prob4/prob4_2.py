# -*- coding: utf-8 -*-
from socket import *
import sys

def main():
    if len(sys.argv[1:]) == 3:
        ip = sys.argv[1]
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    
    else:
        sys.exit()
        
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("error")
        sys.exit()
    
    for port in range(start_port, end_port + 1):
        try:
            # ストリームソケットの作成
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)  # タイムアウトを1秒に設定
            result = s.connect_ex((ip, port))  # ポートに接続を試みる
            if result == 0:  # 接続成功（ポートが開いている）
                print(f"{port}: open")
            else:
                print(f"{port}: time out")
            s.close()
        except error as msg:
            print(f"{port}: {msg}")

if __name__ == "__main__":
    main()