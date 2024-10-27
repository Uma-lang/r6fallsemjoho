#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<int> pos{-1, -1};
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        int a;
        char s;
        cin >> a >> s;
        int hand = (s == 'R');
        if (pos[hand] != -1)
        {
            ans += abs(pos[hand] - a);
        }
        pos[hand] = a;
    }
    cout << ans << endl;
    return 0;
}