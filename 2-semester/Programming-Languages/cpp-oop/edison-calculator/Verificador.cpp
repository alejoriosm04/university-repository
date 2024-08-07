#include <iostream>
#include <string>
#include "Verificador.h"

bool Verificador::verificar(string exp){
    int i=0;
    int parentesis=0;
    while(exp[i]){
        if(parAb(exp[i])){
            parentesis++;
            if (parCerr(exp[i+1]) || (operador(exp[i+1]) && exp[i+1]!='-')){
                return false;
            }
        }else{
            if(numero(exp[i])){
                if (trigon(exp[i+1]) || valorAbs(exp[i+1])){
                    return false;
                }
            }else{
                if(trigon(exp[i])){
                string trig = exp.substr(i,4);
                if(trigonometrica(trig)){
                    i=i+4;                
                    if(parCerr(exp[i])){
                        return false;
                    }
                    if(exp[i]=='-'){
                        i++;
                    }
                    int punto=0;
                    while(exp[i] && !parCerr(exp[i])){
                        if(pun(exp[i])){
                            punto++;
                        }
                        if(!numero(exp[i]) && !pun(exp[i]) && punto>1){
                            return false;
                        }
                        i++;
                    }
                    if(numero(exp[i+1]) || trigon(exp[i+1]) || pun(exp[i+1]) || valorAbs(exp[i+1]) || !exp[i] || parAb(exp[i+1])){
                        return false;
                    }
                }else{
                    return false;
                    }
                }else{
                    if(operador(exp[i])){
                        if(operador(exp[i+1]) || parCerr(exp[i+1]) || !exp[i+1] || (!exp[i-1] && exp[i]!='-')){
                            return false;
                        }
                    }else{
                        if(parCerr(exp[i])){
                            parentesis--;
                            if(parAb(exp[i+1]) || numero(exp[i+1]) || trigon(exp[i+1]) || valorAbs(exp[i+1])){
                                return false;
                            }
                        }else{
                            if(valorAbs(exp[i])){
                                i=i+1;
                                if(valorAbs(exp[i])){
                                    return false;
                                }
                                if(exp[i]==('-')){
                                    i++;
                                }
                                int punto=0;
                                while(exp[i] && !valorAbs(exp[i])){
                                    if(pun(exp[i])){
                                        punto++;
                                    }
                                    if(!numero(exp[i]) && !pun(exp[i]) && punto>1){
                                        return false;
                                    }
                                    i++;
                                }
                                if (!exp[i] || valorAbs(exp[i+1]) || pun(exp[i+1]) || numero(exp[i+1]) || trigon(exp[i+1]) || parAb(exp[i+1])){
                                    return false;
                                }
                            }else{
                                if(pun(exp[i])){
                                    if(!numero(exp[i+1])){
                                        return false;
                                    }
                                }else{
                                    return false;
                                }
                            }
                        }
                    }
                }
            }
        }
        i++;                
    }
    if(parentesis!=0){
        return false;
    }
    return true;
}

bool Verificador::numero(char num){
    switch(num){
        case '0': return true;
            break;
        case '1': return true;
            break;
        case '2': return true;
            break;
        case '3': return true;
            break;
        case '4': return true;
            break;
        case '5': return true;
            break;
        case '6': return true;
            break;
        case '7': return true;
            break;
        case '8': return true;
            break;
        case '9': return true;
            break;
        default: return false;
    }
}
bool Verificador::operador(char oper){
    switch(oper){
        case '+': return true;
            break;
        case '-': return true;
            break;
        case '*': return true;
            break;
        case '/': return true;
            break;
        default: return false;
    }
}
bool Verificador::parAb(char par){
    if(par=='('){
        return true;
    }else{
        return false;
    }
}
bool Verificador::parCerr(char par){
    if(par==')'){
        return true;
    }else{
        return false;
    }
}
bool Verificador::trigon(char letra){
    switch(letra){
        case 'c': return true;
            break;
        case 't': return true;
            break;
        case 's': return true;
            break;
        default: return false;
    }
}
bool Verificador::trigonometrica(string trig){
    if(trig.compare("sen(")!=0 && trig.compare("cos(")!=0 && trig.compare("tan(")!=0){
        return false;
    }else{
        return true;
    }
}
bool Verificador::valorAbs(char valor){
    if(valor=='|'){
        return true;
    }else{
        return false;
    }
}
bool Verificador::pun(char x){
    if(x=='.'){
        return true;
    }else{
        return false;
    }
}
string Verificador::quitarEspacios(string exp){
    string expNueva ="";
    int i=0;
    while(exp[i]){
        if(exp[i]!=' '){
            expNueva+=exp[i];
        }
        i++;
    }
    return expNueva;
}