# -*- coding: utf-8 -*-
import glob

def main():
    path_list = glob.glob('train/**/*.eml') # trainフォルダ内のすべての.emlファイルを取得
    dic = {}  # ユニークな単語を格納する辞書
    
    for file in path_list:
        with open(file, 'rb') as f:
            buf = f.read().decode('utf-8', 'ignore')  # ファイルをUTF-8としてデコード
            buf = buf.lower()  # すべて小文字に変換して大文字小文字を区別しないようにする
            word = ''
            for char in buf:
                if char.isalnum():  # アルファベットまたは数字であれば単語に追加
                    word += char
                else:
                    if word:  # 単語が存在すれば辞書に追加
                        dic[word] = True
                        word = ''  # 単語をリセット
            if word:  # 最後の単語を辞書に追加（ファイルの終わり）
                dic[word] = True

    for word in sorted(dic.keys()):
        print(word)

if __name__ == '__main__':
    main()