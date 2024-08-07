#include <iostream>
#include "Paises.h"
#include <string>
#include "Nodo.h"

using namespace std;

Nodo::Nodo(Pais* data, Nodo* next){
    this->data = data;
    this->next = next;
}
void Nodo::show(){
    cout << "[" << this->data->verDatos() << "]->" << this->next << endl;
}