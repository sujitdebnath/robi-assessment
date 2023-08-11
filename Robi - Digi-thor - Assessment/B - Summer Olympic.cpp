#include <bits/stdc++.h>

using namespace std;

int main(){
    int tcase, year;

    cin >> tcase;

    for(int i=0; i<tcase; i++){
        cin >> year;

        int olympic = (year - 2020) / 4;
        cout << olympic+1 << endl;
    }

    return 0;
}
