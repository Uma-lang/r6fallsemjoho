#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
    string s, t, x;
    int cnt = 0;
    cin >> s >> t;
    vector<string> ans;
    int n = int(s.size());
    while (s != t)
    {
        string nxt(n, 'z');
        for (int i = 0; i < n; i++)
        {
            if (s[i] != t[i])
            {
                string tmp = s;
                tmp[i] = t[i];
                nxt = min(nxt, tmp);
            }
        }
        ans.push_back(nxt);
        s = nxt;
    }
    int sz = ans.size();
    cout << sz << endl;
    for (string e : ans)
        cout << e << endl;
    return 0;
}