# -*- coding: utf-8 -*-
import re

def main():
    urls = [ # 指定されたFQDN（マルウェアの指令サーバ）
        "http://www.sibc.co.jp",
        "http://www.nishina.gr.jp",
        "http://www.araya-kokan.jp"
    ]

    file = "log.txt" # ログファイルを読み込む
    with open(file, 'r', encoding='utf-8') as f:
        buf = f.read().splitlines()

    # 各行を確認し、FQDNが含まれているかどうかをチェック
    for row in buf:
        for url in urls:
            if url in row:
                print(row)
                break  # URLが見つかったらその行を表示して次の行へ進む

if __name__ == "__main__":
    main()