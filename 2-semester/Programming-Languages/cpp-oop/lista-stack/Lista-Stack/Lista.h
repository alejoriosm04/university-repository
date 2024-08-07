#pragma once
#include <iostream> 
#include <string>
#include "Nodo.h"
using namespace std;

class Lista {
    private:
        Nodo* head;
    public:
        Lista() {
            this->head = NULL;
        }
        void push(Nodo* data);
        Nodo* pop();
        void show();

        Nodo* last();
        Nodo* penultimate();
        void show();
};