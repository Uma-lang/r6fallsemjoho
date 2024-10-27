#include <iostream>
#include <string>
using namespace std;

int main()
{
    string S;
    cin >> S;
    if (S.size() >= 4 && S.size() <= 30)
    {
        if (S.substr(S.size() - 3) == "san")
        {
            cout << "Yes" << '\n';
        }
        else
        {
            cout << "No" << '\n';
        }
    }
    else
    {
        cout << "No" << '\n';
    }

    return 0;
}