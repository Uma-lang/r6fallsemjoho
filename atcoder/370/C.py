def main():
    s = input().strip()
    t = input().strip()
    ans = []
    n = len(s)

    while s != t:
        nxt = 'z' * n  # sの長さで'z'を埋めた文字列を初期値に設定
        for i in range(n):
            if s[i] != t[i]:
                tmp = list(s)  # 文字列は直接変更できないのでリストに変換
                tmp[i] = t[i]  # 異なる文字を t の対応する文字に置き換える
                tmp = ''.join(tmp)  # リストを再度文字列に変換
                nxt = min(nxt, tmp)  # 辞書順で最小の文字列を選ぶ
        ans.append(nxt)  # 変換後の文字列を記録
        s = nxt  # sを更新

    sz = len(ans)
    print(sz)
    for e in ans:
        print(e)

if __name__ == "__main__":
    main()