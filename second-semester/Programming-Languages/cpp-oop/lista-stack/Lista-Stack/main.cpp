#include <iostream>
#include <string>
#include "Paises.h"
#include "Nodo.h"
#include "Lista.h"
using namespace std;

int main(){
    /*
    Pais* objP1 = new Pais("Colombia", "Bogota", 51049000);
    Nodo* objNodo = new Nodo(objP1, NULL);
    //cout << "Nodo 1" << endl;
    //objNodo->show();
    
    Nodo* objNodo2 = new Nodo(new Pais("Germany", "Berlin", 80000000), objNodo);
    cout << "--- Nodo 2 ------------------" << endl;
    objNodo2->show();
    objNodo2->next->show();
    */
  
    Lista* pila = new Lista();
    pila->push(new Nodo(new Pais("Colombia","Bogota", 1),NULL));
    pila->push(new Nodo(new Pais("Germany","Berlin", 2),NULL));
    pila->push(new Nodo(new Pais("Francia","Paris", 3),NULL));
    pila->push(new Nodo(new Pais("Peru","Lima", 4),NULL));

    pila->show();
    cout << "---------------" << endl;

    Nodo* x = pila->pop();
    cout << "POP: " ;
    x->show();
    cout << "lista: " << endl;
    pila->show();
    
    return 0;
}