#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<bool> hastaro(N + 1, false);
    int i;
    for (i = 0; i < M; i++)
    {
        int a;
        char b;
        cin >> a >> b;
        if (hastaro[a] == false && b == 'M')
        {
            cout << "Yes" << endl;
            hastaro[a] = true;
        }
        else
        {
            cout << "No" << endl;
        }
    }
    return 0;
}