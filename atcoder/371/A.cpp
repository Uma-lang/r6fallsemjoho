#include <iostream>
using namespace std;

int main()
{
    char S_ab, S_ac, S_bc;
    cin >> S_ab >> S_ac >> S_bc;
    if (S_ab != S_ac)
        cout << 'A' << endl;
    else if (S_ab == S_bc)
        cout << 'B' << endl;
    else
        cout << 'C' << endl;

    return 0;
}