#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int pop_front(vector<int>& vec){
    int el = *vec.begin();
    vec.erase(vec.begin());
    return el;
}

int main() {
    int size;
    vector<int> vec;
    cin>>size;
    for(int i=0; i<size; i++){
        int el;
        cin>>el;
        vec.push_back(el);
    }
    int q1;
    cin>>q1;
    vec.erase(vec.begin()+q1-1);
    int qs,qe;
    cin>>qs>>qe;
    vec.erase(vec.begin()+qs-1, vec.begin()+qe-1);
    cout<<vec.size()<<endl;;
    while(!vec.empty()){
        int el;
        el = pop_front(vec);
        cout<<el<<" ";
    }
    return 0;
}

