# -*- coding: utf-8 -*-
import sys

def main():
    file = "malware.ex_"  # 読み込むバイナリファイルを指定
    with open(file, 'rb') as f:  # バイナリモードでファイルを開く
        buff = f.read()  # ファイル内容をバッファに読み込む
    
    printable = ''
    
    for byte in buff:
        if 32 <= byte <= 126:  # ASCIIの印字可能文字（32から126）の範囲内かチェック
            printable += chr(byte)  # 該当する場合、文字として追加
    
    print(printable)  # 集めた印字可能文字を出力またはmoreコマンドでも可能

if __name__ == "__main__":
    main()