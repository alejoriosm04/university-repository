#include <iostream>
#include <string>
#include "Arbol.h"

Arbol::Arbol(float num){
    this->der=NULL;
    this->izq=NULL;
    this->hijo=NULL;
    this->oper=' ';
    this->func="";
    this->num=num;
}
Arbol::Arbol(){
    this->der=NULL;
    this->izq=NULL;
    this->hijo=NULL;
    this->oper=' ';
    this->func="";
    this->num=0;
}
Arbol::Arbol(char oper,Arbol *izq, Arbol *der){
    this->der=der;
    this->izq=izq;
    this->hijo=NULL;
    this->oper=oper;
    this->func="";
    this->num=0;
}
Arbol::Arbol(string func, Arbol *hijo){
    this->der=NULL;
    this->izq=NULL;
    this->oper=' ';
    this->hijo=hijo;
    this->func=func;
    this->num=0;
}
float Arbol::getNum(){
    return this->num;
}
char Arbol::getOper(){
    return this->oper;
}
Arbol* Arbol::getDer(){
    return this->der;
}
Arbol* Arbol::getIzq(){
    return this->izq;
}
Arbol* Arbol::getHijo(){
    return this->hijo;
}
string Arbol::getFunc(){
    return this->func;
}