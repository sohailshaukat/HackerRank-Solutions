#include <vector>
#include <iostream>

using namespace std;

int main() {
    int arr_count,query_count;
    vector<vector<int>> vectors;
    cin>>arr_count>>query_count;
    int caseId=0;
    while(caseId < arr_count){
        int arr_length;
        cin>>arr_length;
        vector<int> arr;
        for(int i=0; i<arr_length; i++){
            int element;
            cin>>element;
            arr.push_back(element);
        }
        vectors.push_back(arr);
        caseId ++;
    }
    int queryId=0;
    while (queryId < query_count) {
        int arr_index, element_index;
        cin>>arr_index>>element_index;
        cout<<vectors[arr_index][element_index]<<endl;
        queryId ++;
    }
    return 0;
}
