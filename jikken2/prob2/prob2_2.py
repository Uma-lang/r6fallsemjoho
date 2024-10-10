# -*- coding: utf-8 -*-
import zipfile

def main():
    zipfilename = 'test1.zip'  # 解凍対象のZIPファイル
    dictionary = 'dictionary.txt'  # 使用する辞書ファイル

    password = None

    # ZIPファイルのオープン
    zip_file = zipfile.ZipFile(zipfilename)

    # 辞書ファイルを1行ずつ読み込み、各行をパスワードとして試す
    with open(dictionary, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()  # 改行を削除してパスワードを設定

            try:
                # パスワードをバイト形式にエンコードして解凍を試みる
                zip_file.extractall(pwd=password.encode('utf-8'))
                print(f"Password found: {password}")
                return  # 正しいパスワードが見つかったらプログラムを終了
            except:
                # パスワードが間違っていた場合は次のパスワードを試す
                print(f"Wrong password: {password}")

    print("Password not found in dictionary.")

if __name__ == '__main__':
    main()