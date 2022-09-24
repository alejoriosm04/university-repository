#include <iostream>
#include <string>
#include "Paises.h"
#include "Nodo.h"
#include "Lista.h"

using namespace std;

int main() {
    // Pais* objP1 = new Pais("Colombia", "Bogotá", 51049000);
    // Nodo* objNodo = new Nodo(objP1, NULL);
    // cout << "Nodo 1" << endl;
    // objNodo->show();

    // Nodo* objNodo2 = new Nodo(new Pais("Germany", "Berlin", 80000000), objNodo);
    // cout << "------Nodo 2 ----------------" << endl;
    // objNodo2->show();

    // objNodo2->next->show();

    // cout << objP1 -> verDatos() << endl;

    cout << "------------" << endl;
    cout << "PILA" << endl;

    Lista* pila = new Lista();
    pila->push(new Nodo(new Pais("Colombia","Bogota", 1),NULL));
    pila->push(new Nodo(new Pais("Germany","Berlin", 2),NULL));
    pila->push(new Nodo(new Pais("Francia","Paris", 3),NULL));
    pila->push(new Nodo(new Pais("Peru","Lima", 4),NULL));

    pila->show();
    cout << "---------------" << endl;

    Nodo* x = pila->pop();
    cout << "POP: " ;
    cout << "------------" << endl;
    x->show();
    cout << "lista: " << endl;
    pila->show();

    cout << "------------" << endl;
    cout << "COLA" << endl;

    Lista* cola = new Lista();
    cola->add(new Nodo(new Pais("Colombia","Bogota",50), NULL));
    cola->add(new Nodo(new Pais("Germany","Berlin", 2),NULL));
    cola->add(new Nodo(new Pais("Francia","Paris", 3),NULL));
    cola->add(new Nodo(new Pais("Peru","Lima", 4),NULL));

    cola->show();
    cout << "------------" << endl;
    cout << "REMOVE: " ;
    Nodo* elemento = cola->remove();
    elemento->show();

    cout << "-----------" << endl;
    cout << "lista: " << endl;
    cola->show();
    
    return 0;
}