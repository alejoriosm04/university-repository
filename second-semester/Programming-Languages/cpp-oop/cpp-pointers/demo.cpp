#include <iostream>
using namespace std;

void funcionPorReferencia(int *parametro){
    *parametro = *parametro + 10;
    cout << "parametro = " << *parametro << endl;
}

void funcionPorValor(int parametro){
    parametro = parametro + 10;
    cout<< "parametro = " << parametro << endl;
}

// int main(int argc, char* args){
int main(){
    int x = 33; // Definicion de valor
    int *x_adress = &x; // Definicion referencia

    cout << "memoria["<<&x<<"] = "<< x << endl;
    cout << "memoria["<<&x_adress<<"] = "<< x_adress << endl;

    cout << "x = " << &x << endl;

    funcionPorValor(x);
    funcionPorReferencia(x_adress);
    
    return 0;
}