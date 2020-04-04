#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    set<int> s;
    int query_count;
    cin>>query_count;
    while(query_count--){
        int operation, element;
        cin>>operation>>element;
        switch(operation){
            case 1:
                s.insert(element);
                break;
            case 2:
                s.erase(element);
                break;
            case 3:
                cout<<((s.end() == s.find(element)) ? "No" : "Yes" )<<endl;
                break;
        }
    }
    return 0;
}



