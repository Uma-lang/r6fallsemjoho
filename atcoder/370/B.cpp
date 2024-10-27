#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int N;
    cin >> N;
    int genso = 1;
    vector<vector<int>> A(N, vector<int>(N));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cin >> A[i][j];
        }
    }
    for (int i = 0; i < N; i++)
    {
        if (genso - 1 >= i)
        {
            genso = A[genso - 1][i];
        }
        else
        {
            genso = A[i][genso - 1];
        }
    }
    cout << genso << endl;
    return 0;
}