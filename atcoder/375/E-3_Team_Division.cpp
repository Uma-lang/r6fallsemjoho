#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define rep(i,n) for(int i = 0; i < (n); i++)
int main()
{
    int N, A, B;
    int sum_b = 0;
    cin >> N;
    vector<vector<int>> X(3, vector<int>(N));
    rep(i, N){
        cin >> A >>B;
        X[A][i] = X[A][B];
        sum_b += B;
    }
    long long ave = sum_b / N;
    double sum_1 = 0.0, sum_2 = 0.0, sum_3 = 0.0;
    double sub_1, sub_2, sub_3;
    rep(i, N){
        sum_1 += X[0][i];
        sum_2 += X[1][i];
        sum_3 += X[2][i];
    }
    if(ave % 3 == 0){
        sub_1 = (ave > sum_1) ? (ave - sum_1) : (sum_1 - ave);
        sub_1 = (ave > sum_2) ? (ave - sum_2) : (sum_2 - ave);
        sub_1 = (ave > sum_3) ? (ave - sum_3) : (sum_3 - ave);
        rep(i, N){
            if(X[0][i] == sub_1){
                
            }
        }
    }

    return 0;
}