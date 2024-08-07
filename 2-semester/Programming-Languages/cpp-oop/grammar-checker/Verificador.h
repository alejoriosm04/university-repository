#pragma once
#include <iostream>
#include <string>

using namespace std;

class Verificador {
    public:
      bool verificar(string exp);
      bool operador(char caracter);
      bool numero(char caracter);
      
      bool parAbierto(char caracter);
      bool parCerrado(char caracter);
      bool punto(char caracter);

      bool trigon(char letra);
      bool trigonometrica(string trig);
      bool valorAbs(char valor);

      string quitarEspacio(string exp);
};