#include <iostream>
#include <string>
using namespace std;

int main()
{
    int cnt = 0;
    for (int i = 1; i <= 12; i++)
    {
        string S;
        cin >> S;
        if ((int)S.size() == i)
        {
            cnt++;
        }
    }
    cout << cnt << endl;

    return 0;
}
