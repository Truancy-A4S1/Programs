#include <iostream>
#include <string>

using namespace std;

class Student {

    protected:
    string name;
    int year;
    string course;

    public:
    // Constructor, setters and getters
    Student(string name_p, int year_p, string course_p){
        name = name_p;
        year = year_p;
        course = course_p;
    }
    void introduce_yourself(){
        cout << "Hilu I'm " << name << " and I'm studying " << course << " for " << year << " years." << endl;
    }

    string get_name(){
        return name;
    }
    void set_name(string new_name){
        name = new_name;
    }

    int get_year(){
        return year;
    }
    void set_year(int new_year){
        year = new_year;
    }

    string get_course(){
        return course;
    }
    void set_course(string new_course){
        course = new_course;
    }
};

class Infotech : public Student{
    private:
    string fav_language;
    
    public:
    Infotech(string name_p, int year_p, string course_p, string fav_langugae_p)
        :Student(name_p, year_p, course_p)
    {
            fav_language = fav_langugae_p;
    }

    void introduce_yourself(){
        cout << "Hilu I'm " << name << " and I'm studying " << course << " for " << year << " years." << " I write my codes in " << fav_language << endl;
    }

    void set_language(string new_language){
        fav_language = new_language;
    }
    string get_language(){
        return fav_language;
    }
};

class PhysicalEduc: public Student{
    private:
    string sport;

    public:
    PhysicalEduc(string name_p, int year_p, string course_p, string sport_p)
        :Student(name_p, year_p, course_p)
        {
            sport = sport_p;
        }
    void introduce_yourself(){
        cout << "Hilu I'm " << name << " and I'm studying " << course << " for " << year << " years." << " I'd love to play " << sport << " with you." << endl;
    }

    void set_sport(string new_sport){
        sport = new_sport;
    }
    string get_sport(){
        return sport;
    }
};

int main(){

Student std000 = Student("Carl", 2, "Business Administration");
Student std001 = Student("John", 3, "Nursing");

Infotech std002 = Infotech("Mike", 3,"Computer Science","C++");
Infotech std003 = Infotech("Buck", 4,"Information Technology","Python");

PhysicalEduc std004 = PhysicalEduc("Emi",4,"Wellness Management","Sprint");
PhysicalEduc std005 = PhysicalEduc("Hisao",3,"Physical Training","Soccer");

cout << "\n\nStudent : " << endl;
std000.introduce_yourself();
std001.introduce_yourself();

cout << "\n\nInfotech : " << endl;
std002.introduce_yourself();
std003.introduce_yourself();

cout << "\n\nPhysicalEduc : " << endl;
std004.introduce_yourself();
std005.introduce_yourself();


    return 0;
}