#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include "Arbol.h"
#include <math.h>
#include "Analizador.h"

using namespace std;

float Analizador::analizar(Arbol* raiz){
    float res=0;
    if(raiz->getNum()==0 && raiz->getOper()==' ' && raiz->getFunc().compare("")==0){
        return 0;
    }else{
        if(raiz->getNum()!=0){
            return raiz->getNum(); 
        }else{
            if(raiz->getOper()!=' '){
                char operador = raiz->getOper();
                switch(operador){
                    case '+':
                        res = analizar(raiz->getIzq())+analizar(raiz->getDer());
                        break;
                    case '-':
                        res = analizar(raiz->getIzq())-analizar(raiz->getDer());
                        break;   
                    case '*':
                        res = analizar(raiz->getIzq())*analizar(raiz->getDer());
                        break;   
                    case '/':
                        res = analizar(raiz->getIzq())/analizar(raiz->getDer());
                        break;
                }                    
                return res;
            }else{
                char func = raiz->getFunc()[0];
                switch(func){
                    case '|':
                        res = abs(analizar(raiz->getHijo()));
                        break;
                    case 's':
                        res= sin(analizar(raiz->getHijo())*3.14159/180.0);
                        break;
                    case 'c':
                        res= cos(analizar(raiz->getHijo())*3.14159/180.0);
                        break;
                    case 't':
                        res= tan(analizar(raiz->getHijo())*3.14159/180.0);
                        break;
                }
                stringstream stream;
                stream<<fixed<<setprecision(2)<<res;
                float res=stof(stream.str());
                return res;
            }
        }
    }
}