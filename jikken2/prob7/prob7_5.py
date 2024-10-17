import glob
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

def main():
    # ファイルリストを取得
    path_list = glob.glob('train*.eml')
    
    # ラベルを読み込む
    labels = {}
    with open('label.txt', 'r') as f:
        for line in f:
            file_name, label = line.strip().split()
            labels[file_name] = int(label)
    
    # ユニークな単語の辞書を作成
    word_dict = {}
    index = 0
    for path in path_list:
        with open(path, 'rb') as f:
            buf = f.read().decode('utf-8', 'ignore')
            words = buf.lower().split()
            for word in words:
                if word not in word_dict:
                    word_dict[word] = index
                    index += 1
    
    # 特徴ベクトルとラベルを準備
    X = []
    y = []
    for path in path_list:
        file_name = path.split('/')[-1]
        if file_name in labels:
            with open(path, 'rb') as f:
                buf = f.read().decode('utf-8', 'ignore')
                words = buf.lower().split()
                vector = [0] * len(word_dict)
                for word in words:
                    if word in word_dict:
                        vector[word_dict[word]] = 1
                X.append(vector)
                y.append(labels[file_name])
    
    # データを訓練データとテストデータに分割
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)
    
    # Gaussian Naive Bayes モデルを作成して訓練
    clf = GaussianNB()
    clf.fit(x_train, y_train)
    
    # テストデータで精度を評価
    print("Accuracy:", clf.score(x_test, y_test))

if __name__ == '__main__':
    main()