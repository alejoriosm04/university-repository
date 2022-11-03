#pragma once
#include <iostream>
#include <string>
using namespace std;

class Arbol{
    public:
        Arbol(float num);
        Arbol(char oper, Arbol* izq, Arbol* der);
        Arbol(string func, Arbol* num);
        Arbol();
        float getNum();
        char getOper();
        string getFunc();
        Arbol* getDer();
        Arbol* getIzq();
        Arbol* getHijo();

    private:
        Arbol* der;
        Arbol* izq;
        float num;
        char oper;
        string func;
        Arbol* hijo;
};