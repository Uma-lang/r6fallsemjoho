#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    vector<int> X(26);
    string S;
    cin >> S;
    for (int i = 0; i < 26; ++i)
    {
        X[S[i] - 'A'] = i;
    }
    int sum = 0;
    for (int i = 0; i < 25; i++)
    {
        int sub = abs(X[i] - X[i + 1]);
        sum += sub;
    }
    cout << sum << endl;
    return 0;
}