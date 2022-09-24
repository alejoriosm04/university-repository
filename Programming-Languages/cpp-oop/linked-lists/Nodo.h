#pragma once
#include <iostream>
#include "Paises.h"
#include <string>

using namespace std;

class Nodo {
    private:
        Pais* data;

    public:
        Nodo* next;
        Nodo(Pais* data, Nodo* next);
        void show();

};