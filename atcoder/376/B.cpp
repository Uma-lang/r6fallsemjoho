#include <iostream>
#include <vector>
//#include <cmath>
#include<cstdlib>
using namespace std;
int move_number(int n, int from, int to, int ng);
int main()
{
    int n, q;
    cin >> n >> q;
    vector<int> pos{1, 2};
    int hand;
    int cost = 0;
    for (int i = 0; i < q; i++)
    {
        char h;
        int t;
        cin >> h >> t;
        hand = (h == 'R');
        if (hand == 1) // 右手
        {
            cost += move_number(n, pos[1], t, pos[0]);
        }
        else // 左手
        {
            cost += move_number(n, pos[0], t, pos[1]);
        }
        pos[hand] = t;
    }
    cout << cost << endl;
    return 0;
}
/*
int move_number(int n, int from, int to, int ng)
{
    if (from > to)
    {
        swap(from, to);
    }
    if (from < ng and ng < to)
        return n + from - to;
    else
        return to - from;
}
*/
int move_number(int n, int from, int to, int ng)
{
    if (from < ng and ng < to)
        return n - abs(to - from);
    else
        return abs(to - from);
}
