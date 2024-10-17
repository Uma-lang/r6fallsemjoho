# -*- coding: utf-8 -*-
import glob

def main():
    dic = {}
    # label.txtを開く
    with open("label.txt", 'r') as f:
        buf = f.readlines()
        
        # 各行を処理
        for line in buf:
            # ファイル名とラベルを分割（スペースやカンマ区切りを想定）
            file_name, label = line.strip().split()
            
            # 辞書にファイル名をキー、ラベルを値として格納
            dic[file_name] = int(label)

    # 結果を表示（確認用）
    for key, value in dic.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()