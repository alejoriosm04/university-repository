#pragma once
#include <iostream> 
#include <string>
#include "Paises.h"
using namespace std;

class Nodo {
    private:
        Pais* data;
    public:
        Nodo* next;
        Nodo(Pais* data, Nodo* next);
        void show();
};
