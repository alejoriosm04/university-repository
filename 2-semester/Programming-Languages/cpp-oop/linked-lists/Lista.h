#pragma once
#include <iostream>
#include <string>
#include "Nodo.h"

using namespace std;

class Lista{
    private:
        Nodo* head;

    public:
        Lista() {
            this->head = NULL;
        }
        void push(Nodo* data); // Comportamiento pila
        Nodo* pop();

        void add(Nodo* data); // Comportamiento Cola
        Nodo* remove();

        void show();

        Nodo* last();
        Nodo* penultimate();
};