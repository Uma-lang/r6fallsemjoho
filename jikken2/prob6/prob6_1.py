# -*- coding: utf-8 -*-
import re

def main():
    file = "log.txt"
    
    # ログファイルを読み込み
    with open(file, 'rb') as f:
        buf = f.read().splitlines()
    
    fqdn_dict = {}  # 重複を避けるための辞書

    # 正規表現でFQDNを抽出
    fqdn_pattern = re.compile(r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}')
    
    for row in buf:
        try:
            # UTF-8デコード
            row = row.decode('utf-8')
        except:
            continue  # デコードに失敗した行はスキップ
        
        # FQDNを正規表現で抽出
        matches = fqdn_pattern.findall(row)
        
        # FQDNを辞書に追加（重複を防ぐ）
        for fqdn in matches:
            fqdn_dict[fqdn] = True  # FQDNがあればTrue、重複しない

    # ユニークなFQDNを表示
    for fqdn in sorted(fqdn_dict.keys()):
        print(fqdn)

if __name__ == "__main__":
    main()