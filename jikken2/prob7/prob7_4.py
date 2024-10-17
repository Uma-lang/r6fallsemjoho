# -*- coding: utf-8 -*-
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

def main():
    iris = datasets.load_iris()  # irisのデータセットをロード
    X = iris.data  # 特徴ベクトルを取得
    y = iris.target  # ラベルを取得
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)  # 訓練データとテストデータに分離
    
    clf = GaussianNB()  # 単純ベイズモデルの作成
    clf.fit(x_train, y_train)  # 訓練データを用いてモデルを訓練
    print(clf.score(x_test, y_test))  # テストデータの分類精度を表示

if __name__ == '__main__':
    main()