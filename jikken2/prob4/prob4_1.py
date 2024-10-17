# -*- coding: utf-8 -*-
from socket import *
import sys

def main():
    if len(sys.argv[1:]) == 2:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        exit()
    try:
        #ストリームソケットの作成
        s = socket(AF_INET, SOCK_STREAM, 0)
        s.settimeout(1)
        s.connect((ip, port))
        print(str(port) + ':open')
        s.close()
    except error as msg:
        print(str(port) + ':' + str(msg))
        
if __name__ == "__main__":
    main()