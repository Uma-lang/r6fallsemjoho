#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    vector<int> B(N);
    int maxA = INT_MIN, maxB = INT_MIN;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
        maxA = max(maxA, A[i]);
    }
    for (int i = 0; i < N; i++)
    {
        cin >> B[i];
        maxB = max(maxB, B[i]);
    }
    cout << maxA + maxB << endl;
    return 0;
}