#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    int size;
    vector<int> vec;
    string str;
    
    cin>>size;
    while(size--){
        int el;
        cin>>el;
        vec.push_back(el);
    }
    int queries;
    cin>>queries;
    for(int i=0; i<queries; i++){
        int q;
        vector<int>::iterator low;
        cin>>q;
        low = lower_bound(vec.begin(),vec.end(),q);
        if (q==*low){
            cout<<"Yes ";
        }
        else{
            cout<<"No ";
        }
        cout<<(low-vec.begin()+1)<<endl;
    }
    return 0;
}

