#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string S;
    cin >> S;
    S.erase(remove(S.begin(), S.end(), '.'), S.end());
    cout << S << endl;
    return 0;
}