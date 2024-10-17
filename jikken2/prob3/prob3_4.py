# -*- coding: utf-8 -*-

def main():
    file = "malware.ex_"  # 読み込むファイルの名前
    with open(file, 'rb') as f:  # バイナリモードでファイルを開く
        buf = f.read()  # ファイルの内容をすべて読み込む（バイト列）

    plaintext = 'www.practicalmalwareanalysis.com'  # 検索する文字列
    possible_keys = range(256)  # 0x00から0xFFまでのすべてのXORキー

    for xor_key in possible_keys:
        xor_encode = [] #アドレスをエンコードした値を格納する、毎回ここでリストをリセットしている
        for char in plaintext:
            encode_char = ord(char) ^ xor_key #xorエンコード
            xor_encode.append(encode_char) #リストに追加
        
        encode_byte = bytes(xor_encode) #xor_encodeはリストオブジェクトなので、バイト列に変換
        index = buf.find(encode_byte) # エンコードされたバイト列をファイル内で検索
        if index != -1: #もし一致したら
            print(f"XORキー: 0x{xor_key:02X}, オフセット: {index}")

if __name__ == "__main__":
    main()