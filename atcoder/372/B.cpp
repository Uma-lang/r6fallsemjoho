#include <iostream>
#include <vector>
using namespace std;
/*
int main()
{
    int M;
    cin >> M;
    int i, k;
    vector<int> A;
    for (k = 0; k <= 10; k++)
    {
        for (i = 0; i < (M % 3); i++)
        {
            A.push_back(k);
        }
        M /= 3;
    }
    cout << A.size() << endl;
    for (i = 0; i < A.size(); i++)
    {
        cout << A[i]  << " \n"[i == A.size() - 1];
    }
    cout << endl;
    return 0;
}
*/

int main()
{
    int M;
    cin >> M;
    int i = 0, sho, amari, m = M;
    vector<int> X;

    while(m != 0)
    {
        sho = m / 3;
        amari = m % 3;
        X.push_back(amari);
        i++;
        m = sho;
    }
    cout << i << endl;
    for(int j = i - 1; j >= 0; j--)
    {
        cout << X[j] << ' ';
    }
    cout << endl;

    return 0;
}