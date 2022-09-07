#include <iostream>
#include <string>
#include "Paises.h"
// Otras librerias

using namespace std;

Pais::Pais(string nombre, string capital, int poblacion) {
    this -> nombre = nombre;
    this -> capital = capital;
    this -> poblacion = poblacion;
}
Pais::Pais() {
    this -> nombre = "Sin nombre";
    this -> capital = "Sin capital";
    this -> poblacion = 0;
}
void Pais::setPoblacion(int valor) {
    this -> poblacion = valor;
}
string Pais::verDatos() {
    string valor = "Pais: ";
    valor = valor + this -> nombre + " (" + this -> capital + ", poblacion: " + to_string(this -> poblacion) + ")";
    return valor;
}