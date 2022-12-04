#include <iostream>
#include <string>
#include "Verificador.h"

using namespace std;

int main(){
    cout << "Ingrese la expresion: " << endl;
    string exp="";
    getline(cin, exp);

    cout << "La expresion es: " << exp << endl;

    // Verificador* scan = new Verificador();
    // exp = scan->verificar(exp);
    // exp = scan->quitarEspacio(exp);
    // cout << "Sin espacios: " << exp << endl;
    // bool gramaticaOk = scan->verificar(exp);
    // cout << " varificar scan: " << gramaticaOk << endl;

    Verificador* scan = new Verificador();
    string exp2 = scan->quitarEspacio(exp);
    cout << "Sin espacios: " << exp2 << endl;
    bool varVerificador = scan->verificar(exp2);
    cout << " varificar scan: " << varVerificador << endl;
}