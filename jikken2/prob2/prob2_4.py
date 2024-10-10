# -*- coding: utf-8 -*-
import zipfile

# 再帰関数：全ての組み合わせを試す
def recur(password, length):
    zipfilename = 'test3.zip'  # 解凍するZIPファイル名
    zip_file = zipfile.ZipFile(zipfilename)

    # 英数字の文字セット（0-9, a-z, A-Z）
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 現在のパスワードが指定された長さに達した場合、解凍を試みる
    if len(password) == length:
        try:
            # パスワードをバイト形式にエンコードして解凍を試みる
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"Password found: {password}")
            return True  # 正しいパスワードが見つかったら終了
        except:
            return False  # パスワードが間違っていた場合はFalseを返す

    # 次のパスワード候補を生成（0-9, a-z, A-Zの各文字を追加）
    for char in chars:
        next_password = password + char
        # 再帰的に次のパスワードを試す
        if recur(next_password, length):
            return True  # パスワードが見つかったら再帰を終了

    return False  # 全ての組み合わせを試しても見つからなかった場合

# メイン関数
def main():
    length = 3  # 試すパスワードの長さ（例：3桁）
    password = ""  # 初期のパスワードを空文字列に設定
    recur(password, length)  # 再帰関数を呼び出して全ての組み合わせを試す

if __name__ == '__main__':
    main()