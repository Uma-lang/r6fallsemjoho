#include <iostream>
#include <string>
using namespace std;

bool is_abc(const string &S, int i) { return(S[i] == 'A' && S[i + 1] == 'B' && S[i + 2] == 'C'); }

int main()
{
    string S;
    int N, Q, x;
    int sum = 0, idx;
    char c;

    cin >> N >> Q; // 文字列の長さとクエリ数の入力
    cin >> S;      // 文字列の入力

    // 最初に文字列全体に含まれる "ABC" の数をカウント
    for (int i = 0; i <= N - 3; i++)
    {
        if (is_abc(S, i))
        {
            sum += 1;
        }
    }

    // 各クエリを処理
    for (int i = 0; i < Q; i++)
    {
        cin >> x >> c; // インデックスと新しい文字の入力
        x -= 1;        // 0ベースのインデックスに変換

        // 変更前に "ABC" の影響を除去
        for (int j = 0; j < 3; j++)
        {
            idx = x - j;
            if (idx >= 0 && idx <= N - 3 && is_abc(S, idx))
            {
                sum -= 1;
            }
        }

        // 文字列を更新
        S[x] = c;

        // 変更後に "ABC" の影響を再追加
        for (int j = 0; j < 3; j++)
        {
            idx = x - j;
            if (idx >= 0 && idx <= N - 3 && is_abc(S, idx))
            {
                sum += 1;
            }
        }

        // 結果を出力
        cout << sum << endl;
    }

    return 0;
}