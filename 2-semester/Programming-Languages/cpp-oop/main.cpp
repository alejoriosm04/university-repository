#include <iostream>
using namespace std;

int suma(int a, int b){
  int c = a + b;
  return c;
}

int main() {
    cout << "Hello World!" << endl;
    int a;
    cout << "Valor de A: ";
    cin >> a;
    int b;
    cout << "Valor de B: ";
    cin >> b;
    int c = suma(a, b);
    cout << "a + b = " << c << endl;
}