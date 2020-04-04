#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int query_count;
    map<string, int> record;
    cin>>query_count;
    while(query_count--){
        int operation;
        string name;
        cin>>operation>>name;
        switch(operation){
            case 1:
                int marks;
                cin>>marks;
                if(record.find(name)==record.end()){
                    record.insert(make_pair(name,marks));    
                }else{
                    record[name]+=marks;
                }
                break;
            case 2:
                record.erase(name);
                break;
            case 3:
                cout << ( (record.find(name)==record.end()) ? 0 : record[name] ) << endl;   
                break;
        }

    }

    return 0;
}
