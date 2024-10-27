#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n, c;
    cin >> n >> c;
    vector<int> t(n);
    for (int &i : t)
    {
        cin >> i;
    }
    int ame = 1;
    int pre = t[0];
    for (int i = 1; i < n; i++)
    {
        if (t[i] - pre >= c)
        {
            ame += 1;
            pre = t[i];
        }
    }
    cout << ame << endl;
    return 0;
}