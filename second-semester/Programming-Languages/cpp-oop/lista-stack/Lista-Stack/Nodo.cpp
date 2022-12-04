#include <iostream> 
#include <string>
#include "Paises.h"
#include "Nodo.h"
using namespace std;

Nodo :: Nodo(Pais* data, Nodo* next){
    this->data = data;
    this->next = next;
}

void Nodo::show(){
    cout << "["<< this->data->verDatos() <<"]->" 
         << this->next << endl;
}

