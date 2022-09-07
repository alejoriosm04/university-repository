#include <iostream>
#pragma once
#include <string>
// Otras librerias

using namespace std;

class Pais {
    // Privados
    private:
        string nombre;
        string capital;
        int poblacion;

    // Publicos
    public:
        Pais(string nombre, string capital, int poblacion);
        Pais();
        void setPoblacion(int valor);
        string verDatos();

};