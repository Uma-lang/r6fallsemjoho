
# 入力の取得
N = int(input())
S = input()

count = 0
# 1 から N-2 の範囲で条件を満たすかチェック
for i in range(1, N - 1):
    if S[i - 1] == '#' and S[i] == '.' and S[i + 1] == '#':
        count += 1

# 結果の出力
print(count)