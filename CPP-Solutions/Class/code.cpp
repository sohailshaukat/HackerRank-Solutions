#include <iostream>
#include <sstream>
#include <string>
using namespace std;

class Student{
    private:
        int age;
        int standard;
        string first_name;
        string last_name;
    public:
        void set_age(int new_age);
        void set_standard(int standard);
        void set_first_name(string new_first_name);
        void set_last_name(string last_name);
        int get_age();
        int get_standard();
        string get_first_name();
        string get_last_name();
        string to_string(){
            string a = std::to_string(age);
            string s = std::to_string(standard);
            return(a+","+first_name+","+last_name+","+s);
        }
};

void Student::set_age(int new_age){
    age = new_age;
}
void Student::set_standard(int new_standard){
    standard = new_standard;
}
void Student::set_first_name(string new_first_name){
    first_name = new_first_name;
}
void Student::set_last_name(string new_last_name){
    last_name = new_last_name;
}

int Student::get_age(){
    return(age);
}
int Student::get_standard(){
    return(standard);
}
string Student::get_first_name(){
    return(first_name);
}
string Student::get_last_name(){
    return(last_name);
}



int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
