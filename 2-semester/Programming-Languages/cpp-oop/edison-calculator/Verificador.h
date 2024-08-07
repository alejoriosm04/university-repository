#pragma once
#include <iostream>
#include <string>

using namespace std;

class Verificador{
    public:
        bool verificar(string exp);
        bool operador(char oper);
        bool numero(char num);
        bool trigon(char letra);
        bool trigonometrica(string trigo);
        bool valorAbs(char valor);
        bool parAb(char par);
        bool parCerr(char par);
        bool pun(char punt);
        string quitarEspacios(string exp);
    private:
};