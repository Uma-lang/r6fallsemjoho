#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> K(N);
    int sumTotal = 0;
    for (int i = 0; i < N; ++i)
    {
        cin >> K[i];
        sumTotal += K[i];
    }

    int minDifference = sumTotal;
    // 全ての組み合わせをビットマスクで試す (1 << N は 2^N)
    for (int mask = 0; mask < (1 << N); ++mask)
    {
        int sumA = 0;
        for (int i = 0; i < N; ++i)
        {
            if (mask & (1 << i))
            {
                sumA += K[i];
            }
        }
        int sumB = sumTotal - sumA;
        int maxGroupSize = max(sumA, sumB);
        minDifference = min(minDifference, maxGroupSize);
    }

    cout << minDifference << endl;
    return 0;
}