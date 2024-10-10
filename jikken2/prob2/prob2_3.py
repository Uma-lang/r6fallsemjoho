# -*- coding: utf-8 -*-
import zipfile
        
def main():
    zipfilename = 'test2.zip'  # 解凍対象のZIPファイル名
    zip_file = zipfile.ZipFile(zipfilename)  # ZIPファイルを開く
        
    # 2桁の数字の全組み合わせ（00～99）を試す
    for i in range(100):
        password = f"{i:02d}"  # 2桁の文字列に変換（例：1 → '01'）
        
        try:
            # パスワードをバイト形式にエンコードして解凍を試みる
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"Password found: {password}")  # 正しいパスワードが見つかった場合
            return  # パスワードが見つかったらプログラムを終了
        except:
            # パスワードが間違っていた場合は次のパスワードを試す
            print(f"Wrong password: {password}")
        
    print("Password not found in the range 00-99.")  # すべてのパスワードを試しても見つからなかった場合
        
if __name__ == '__main__':
    main()