#include <iostream>
using namespace std;

int sum_of_even_numbers(int inn){
    int result = 0;
    cout << "Even numbers are: ";
    for(int i=1; i<=inn; i++){
        result = result + (i * 2);
        cout << i * 2 << " ";
    }
    cout << endl;

    return result;
}

int main(){
    int in;
    cout << "Input number of terms: ";
    cin >> in;  

    cout << "Sum of even numbers up to " << in << "th term: " << sum_of_even_numbers(in) << endl;
    return 0;
}