# -*- coding: utf-8 -*-
import glob

def main():
    # trainフォルダのすべてのeml拡張子のファイルのリストを取得
    path_list = glob.glob('train/**/*.eml')
    for file in path_list:
        print(file)
        with open(file, 'rb') as f:
            buf = f.readlines()
            for row in buf:
                print(row.decode("utf-8", "ignore"))

if __name__ == '__main__':
    main()