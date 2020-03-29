#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int pop_front(vector<int>& vec)
{
    int el;
    el = *vec.begin();
    vec.erase(vec.begin());
    return el;
}

int main() {
    vector<int> v;
    int size,el;
    cin>>size;
    for(int i=0; i<size; i++){
        cin>>el;
        v.push_back(el);
    }
    sort(v.begin(),v.end());
    for(int i=0; i<size; i++){
        el = pop_front(v);
        cout<<el<<" ";
    }   
    return 0;
}