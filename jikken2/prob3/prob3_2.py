# -*- coding: utf-8 -*-
import string, base64
'''
def main():
    s = "aG9zdG5hbWUtZm9v"
    ds = base64.decodestring(s.encode('utf-8'))# base64.decodestring()は非推奨
    print(ds.decode('utf-8'))
'''
def main():
    s = "aG9zdG5hbWUtZm9v"
    ds = base64.b64decode(s.encode('utf-8'))
    print(ds.decode('utf-8'))

if __name__ == "__main__":
    main()
    
    