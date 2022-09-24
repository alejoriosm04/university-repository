#pragma once
#include <iostream> 
#include <string>
using namespace std;

class Pais {
  private:
  string nombre;
  string capital;
  int poblacion;
  
  public:
  Pais(string nombre, string capital, int poblacion);
  Pais();
  void setPoblacion(int valor);
  string verDatos();
};