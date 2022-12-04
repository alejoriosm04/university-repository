#include <iostream>
#include <string>
#include "Arbol.h"
#include "Verificador.h"
#include "Constructor.h"

Arbol* Constructor::construir(string exp){
    exp="("+exp+")";
    exp=quitarPar(exp);
    int pos=divisiones(exp);
    if(pos==0){
        if(letra->numero(exp[1])){
            Arbol* ar = new Arbol(stof(exp.substr(1,exp.size()-2)));
            return ar;
        }
        if(letra->trigon(exp[1]) || letra->valorAbs(exp[1])){
            string num="";
            int i = 1;
            while(exp[i]){
                if(letra->numero(exp[i]) || exp[i]=='-' || letra->pun(exp[i])){
                    num+=exp[i];
                }
                i++;
            }
            string func="";
            switch(exp[1]){
                case 's': func="sen";
                    break;
                case 't': func="tan";
                    break;
                case 'c': func="cos";
                    break;
                case '|': func="| |";
                    break;
            }
            Arbol* arNum = new Arbol(stof(num));
            Arbol* ar=new Arbol(func,arNum);
            return ar; 
        }
    }else{
        Arbol* ar = new Arbol(exp[pos],construir(exp.substr(1,pos-1)),construir(exp.substr(pos+1,(exp.size()-1)-(pos+1))));
        return ar;
    }
    Arbol* ar = new Arbol();
    return ar;
}

int Constructor::divisiones(string exp){
    int i=0;
    int cont=-1;
    char oper=' ';
    int pos=0;
    while(exp[i]){
        if(letra->parAb(exp[i])){
            cont++;
        }
        if(letra->parCerr(exp[i])){
            cont--;
        }
        if(cont==0){
            if(letra->operador(exp[i])){
                if(exp[i]=='-' && (letra->valorAbs(exp[i-1]))){}
                else{
                    if(exp[i]=='+' || exp[i]=='-'){
                        oper = exp[i];
                        pos=i;
                    }else{
                        if(oper==' '){
                            oper=exp[i];
                            pos=i;
                        }
                    }
                }
            } 
        }
        i++;
    }
    return pos;
}

string Constructor::quitarPar(string exp){
    int i=0;
    int cont=0;
    bool quitar=false;
    if(exp[1]!='('){
        return exp;
    }else{
        while(exp[i]){
            if(exp[i]=='('){
                cont+=1;
            }
            if(exp[i]==')'){
                cont-=1;
            }            
            if(cont==1 && letra->operador(exp[i])){
                return exp;
            }else{
                if(cont==0){
                    return quitarPar(exp.substr(1,(exp.size()-2)));
                }
            }
            i+=1;
        }       
    }
}