#include <iostream>
#include <string>
#include "Verificador.h"

using namespace std;

int main(){
    cout << "Ingrese la expresion: " << endl;
    string exp="";
    getline(cin, exp);

    cout << "usted escribrio la expr: " << exp << endl;

    Verificador* scan = new Verificador();
    //string exp2 = scan->quitarEspacio(exp);
    //cout << "exp sin espacios: " << exp2 << endl;
    bool varVerificar = scan->verificar(exp);
    if (varVerificar){
        cout << "Expresion valida..." << endl;
    } else {
        cout << "Expresion en silla de ruedas :)" << endl;
    }
    //exp = scan->quitarEspacio(exp);
    //cout << "Sin espacios: " << exp << endl;
    //bool gramaticaOk = scan->verificar(exp);
    //cout << " varificar scan: " << gramaticaOk << endl;
}