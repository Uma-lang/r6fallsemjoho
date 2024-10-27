#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int N = 10;
    //char S[] = "FHAEEFHUIAREHFNAERFRAGEHFKGAUGJECBTQOYETCBYQUWROLQUWYETGRFBCUQLEOWIUAYXNAUWEIYRUQWIEYRBCQIUWERYVIUAW\0";
    char S[N + 1];
    for(int i = 0; i < N; i++){
        cin >> S[i];
    }
    S[N] = '\0';
    int cnt = 0;
    int length = strlen(S);
    for(int i = 0; i < length; i++){
        for(int j = i + 1; j < length; j++){
            if(S[i] == S[j]){
                cnt++;
            }
        }
    }

    cout << cnt << '\n';

    return 0;
}