#pragma once
#include <iostream>
#include <string>
#include "Verificador.h"
#include "Arbol.h"

using namespace std;

class Constructor{
    public:
        Constructor(){letra=new Verificador();}
        Arbol* construir(string exp);
        int divisiones(string exp);
        string quitarPar(string exp);
    private:
        Verificador* letra;
};