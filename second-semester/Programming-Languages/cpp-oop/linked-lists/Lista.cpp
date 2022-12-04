#include <iostream>
#include <string>
#include "Nodo.h"
#include "Lista.h"

using namespace std;

void Lista::push(Nodo* data){
    data->next = this->head;
    this->head = data;
}

Nodo* Lista::pop(){
    Nodo* tmp = this->head;
    this->head = this->head->next;
    return tmp;
}

Nodo* Lista::last(){
    Nodo* a_last = this->penultimate();
    if (a_last) {
        return a_last->next;
    } else {
        a_last = this->head;
    }
    return a_last;
}

Nodo* Lista::penultimate(){
    Nodo* p_last = this->head;
    // Verificacion que la lista no es vacia
    if (p_last != NULL) {
        // Verificacion lista es de un solo elemento
        if (p_last->next) {
            while(p_last->next->next != NULL){
                p_last = p_last->next;
            }
            return p_last;
        } else {
            cout << "La lista es de un solo elemento, no tiene antepenultimo" << endl;
            return NULL;
        }
    }
    cout << "La lista es vacía" << endl;
    return NULL;
}

void Lista::show(){
    Nodo* aux = this->head;
    while(aux){
        aux->show();
        aux = aux->next;
    }
}

void Lista::add(Nodo* data){
    this->push(data);
}

Nodo* Lista::remove(){
    Nodo* last = this->last();
    this->penultimate()->next = NULL;
    return last;
}