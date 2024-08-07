#include <iostream>
#include <string>
#include "Constructor.h"
#include "Verificador.h"
#include "Arbol.h"

Arbol* Constructor::construir(string exp){
    exp = "(" + exp + ")";
    exp = quitarParentesis(exp);
    int ramas = rama(exp);
    if (ramas == 0){ // si no tengo ramas
        if (letra->numero(exp[1])){
            Arbol* ar = new Arbol(stof(exp.substr(1, exp.size()-2)));
            return ar;
        }
        if (letra->trigon(exp[1]) || letra->valorAbs(exp[1])){ // significa que el operador es unuario
            string num = "";
            int i = 1;
            while(exp[i]){
                if (letra->numero(exp[i]) || exp[i] == '-' || letra->punto(exp[i])){
                    i++;
                }
            }
            string func = "";
            switch (exp[i]){
                case 's': 
                func = "sen";
                break;

                case 'c':
                func = "cos";
                break;

                case 't':
                func = "tan";
                break;
            }
            Arbol* arNum = new Arbol(stof(num));
            Arbol* ar = new Arbol(func, arNum);
            return ar;
        }
    } else { // caso contrario, si tengo ramas

    }

}
int Constructor::rama(string exp){

}
string Constructor::quitarParentesis(string exp){

}