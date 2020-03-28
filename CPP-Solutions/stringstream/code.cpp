#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    vector<int> v;
    istringstream ss(str); 
    int i;
    char ch;
    while(ss>>i)
    {
        // cout<<i<<endl;  
        v.push_back(i);
        ss>>ch;
    }   
    return v; 
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

