#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    char S[n];
    for (int i = 0; i < n; i++)
    {
        cin >> S[i];
    }

    int count = 0;
    for (int i = 0; i < n - 2; i++)
    {
        if (S[i] == '#' && S[i + 1] == '.' && S[i + 2] == '#')
        {
            count++;
        }
    }

    cout << count;

    return 0;
}