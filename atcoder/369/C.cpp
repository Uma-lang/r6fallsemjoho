#include <iostream>
#include <vector>
using namespace std;
long long sum_n(long long n) { return n * (n + 1) / 2; }
int main()
{
    int n;
    cin >> n;
    long long ans = n;
    int pre = 0;
    vector<int> a(n);
    for (int &i : a)
        cin >> i;
    for (int i = 1; i < n - 1; i++)
    {
        if (a[i] - a[i - 1] != a[i + 1] - a[i])
        {
            ans += sum_n(i - pre);
            pre = i;
        }
    }
    ans += sum_n(n - 1 - pre);
    cout << ans << endl;
    return 0;
}