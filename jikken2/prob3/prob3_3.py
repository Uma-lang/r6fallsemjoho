# -*- coding: utf-8 -*-
import string #asciiコードを使うため

def main():
    file = "malware.ex_"  # 読み込むファイルの名前
    with open(file, 'rb') as f:  # バイナリモードでファイルを開く
        buf = f.read()  # ファイルの内容をすべて読み込む(バイト列)
    
    xor_key = 0x3B  # XORに使用するキー
    
    plaintext = 'www.practicalmalwareanalysis.com' #検索するアドレス
    xor_encode = [] #アドレスをエンコードした値を格納する
    for char in plaintext:
        encode_char = ord(char) ^ xor_key #xorエンコード
        xor_encode.append(encode_char) #リストに追加
        
    encode_byte = bytes(xor_encode) #xor_encodeはリストオブジェクトなので、バイト列に変換
    index = buf.find(encode_byte) #findメソッドでencode_byteを検索
    print(f"オフセット:{index}")

if __name__ == "__main__":
    main()