#include <iostream>
#include <string>
#include "Analizador.h"
#include "Arbol.h"
#include "Verificador.h"
#include "Constructor.h"

using namespace std;

int main(int argc, char* argv[]){
    cout<<"Ingresa una expresion"<<endl;
    string expr="";
    getline(cin, expr);
    Verificador *veri= new Verificador();
    expr= veri->quitarEspacios(expr);
    bool hacer=veri->verificar(expr);
    while(!hacer){
        cout<<"Ingrese una expresion valida"<<endl;
        getline(cin, expr);
        expr = veri->quitarEspacios(expr);
        hacer=veri->verificar(expr);
    }
    Constructor* cons = new Constructor();
    Arbol* arbol = cons->construir(expr);
    Analizador* anal = new Analizador();
    float res=anal->analizar(arbol);
    cout<<res<<endl;
    delete anal;
    delete arbol;
    delete cons;   
    delete veri;
}