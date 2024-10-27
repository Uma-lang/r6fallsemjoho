def main():
    # 入力
    n = int(input())
    a = [list(input().strip()) for _ in range(n)]

    # 回転後の結果を格納する配列
    ans = [[''] * n for _ in range(n)]

    # 各マスを距離 d に基づいて回転
    for i in range(n):
        for j in range(n):
            # 手動で4つの値の最小値を求める
            d = i
            if j < d:
                d = j
            if n - 1 - i < d:
                d = n - 1 - i
            if n - 1 - j < d:
                d = n - 1 - j

            rotations = d % 4

            ni, nj = i, j
            for _ in range(rotations):
                ni, nj = nj, n - 1 - ni

            ans[ni][nj] = a[i][j]

    # 結果の出力
    for i in range(n):
        print("".join(ans[i]))

if __name__ == "__main__":
    main()