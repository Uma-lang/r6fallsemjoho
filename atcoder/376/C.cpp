#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> a(n), b(n - 1);
    for (int &i : a)
        cin >> i;
    for (int &i : b)
        cin >> i;
    sort(a.begin(), a.end());
    int ok = 1 << 30, ng = 0;
    auto f = [&](int x) -> bool
    {
        vector<int> nb = b;
        nb.push_back(x);
        sort(nb.begin(), nb.end());
        for (int i = 0; i < n; i++)
        {
            if (a[i] > nb[i])
                return false;
        }
        return true;
    };
    if (!f(ok))
    {
        cout << -1 << endl;
        return 0;
    }
    while (ok - ng > 1)
    {
        int mid = (ok + ng) / 2;
        if (f(mid))
            ok = mid;
        else
            ng = mid;
    }
    cout << ok << endl;
}
