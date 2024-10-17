# -*- coding: utf-8 -*-
import re

def main():
    # マルウェアとその通信パターン（シグネチャ）の辞書
    signatures = {
        "EMDIVI": [
            "/app/plugins/index.php",
            "/local/index.php",
            "/www/index.php",
            "/book/index.php",
            "/state/index.php",
            "/folder/index.php",
            "/look/index.php",
            "/common/index.php"
        ],
        "PoizonIvy": [
            "kkol.pokemonn.net/fndex.html"
        ]
    }

    # ログファイルを読み込み
    file = "log.txt"
    with open(file, 'r', encoding='utf-8') as f:
        buf = f.read().splitlines()

    # 各行を検索してマルウェアパターンを探す
    for i, row in enumerate(buf, start=1):  # 行番号を1から始める
        for malware, patterns in signatures.items():
            for pattern in patterns:
                if pattern in row:
                    print(f"found malware string {pattern} for {malware} in line {i}")# : {row}")

if __name__ == "__main__":
    main()