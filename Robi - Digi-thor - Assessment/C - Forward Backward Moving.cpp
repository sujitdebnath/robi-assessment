# include<bits/stdc++.h>

using namespace std;

int main(){
    int arrSz, rotateN, rotateT;

    cin >> arrSz >> rotateN >> rotateT;

    vector<int> vec;

    for(int i=0; i< arrSz; i++){
        int elem;
        cin >> elem;
        vec.push_back(elem);
    }

    if(rotateT == 0){
        rotate(vec.begin(), vec.begin()+rotateN, vec.end());
    }
    else{
        for(int i=0; i<rotateN; i++)
            rotate(vec.begin(), vec.end()-1, vec.end());
    }

    for(int i=0; i< arrSz-1; i++)
        cout << vec[i] << " ";
    cout << vec[arrSz-1];

    return 0;
}
