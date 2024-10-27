#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    if ((a - b) % 2 == 0)
    {
        cnt += 1;
    }
    if (a != b)
    {
        cnt += 2;
    }
    if (a == b)
    {
        cnt = 1;
    }
    cout << cnt << endl;
    return 0;
}