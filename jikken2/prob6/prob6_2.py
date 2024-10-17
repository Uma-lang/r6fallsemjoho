# -*- coding: utf-8 -*-
import re

def main():
    file = "log.txt"
    
    # ログファイルを読み込み
    with open(file, 'rb') as f:
        buf = f.read().splitlines()
    
    post_count = 0  # POSTメソッドの連続回数をカウント
    post_lines = []  # POSTが連続した行を保存するリスト
    
    for row in buf:
        try:
            # UTF-8デコード
            row = row.decode('utf-8')
        except:
            continue  # デコードに失敗した行はスキップ
        
        # 行にPOSTメソッドが含まれているかを確認
        if "POST" in row:
            post_count += 1
            post_lines.append(row)
        else:
            # POSTの連続が途切れたら、連続回数を確認して10回以上であれば出力
            if post_count >= 10:
                print(f"連続して {post_count} 回POSTが実行されました:")
                for line in post_lines:
                    print(line)
                print("-" * 50)
            
            # カウントとリストをリセット
            post_count = 0
            post_lines = []

    # 最後の連続回数が10回以上の場合も処理
    if post_count >= 10:
        print(f"連続して {post_count} 回POSTが実行されました:")
        for line in post_lines:
            print(line)
        print("-" * 50)

if __name__ == "__main__":
    main()