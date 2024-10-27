#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string S;
    string T;

    cin >> S;
    cin >> T;

    int n = min(S.size(), T.size());

    for (int i = 0; i < n; i++)
    {
        if (S[i] != T[i])
        {
            cout << i + 1 << '\n';
            return 0;
        }
    }

    if (S.size() != T.size())
    {
        cout << n + 1 << '\n';
    }
    else
    {
        cout << 0 << '\n';
    }

    return 0;
}