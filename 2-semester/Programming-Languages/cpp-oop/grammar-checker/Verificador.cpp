#include <iostream>
#include <string>
#include "Verificador.h"

bool Verificador::verificar(string exp){ 
    cout << "{ver 1} recibe: "<< exp << endl;
    int i=0;
    int parentesis = 0;
    while (exp[i]){
       cout << "{ver 2} procesa: "<< exp[i] << endl;
       if (parAbierto(exp[i])){
          parentesis++;
          cout << "{ver 3} total parentesis: "<< parentesis << endl;
          if( parCerrado(exp[i+1]) || (operador(exp[i+1]) && exp[i+1]!='-') || !exp[i+1]) {
             return false;
          }
       } else {
            if (numero(exp[i])) {
                if (trigon(exp[i+1]) || valorAbs(exp[i+1])){
                  return false;
                } else {
                  if(trigon(exp[i+1])){
                    string trig = exp.substr(i,4);
                    if (trigonometrica(trig)){
                      i=i+4;
                      if (parCerrado(exp[i])){
                        return false;
                      }
                      if (exp[i]=='-'){
                        i++;
                      }
                      int valorPunto=0;
                      while(exp[i] && !parCerrado(exp[i])){
                        if (punto(exp[i])){
                            valorPunto++;
                        } 
                        if (!numero(exp[i]) && !punto(exp[i]) && valorPunto>1){
                          return false;
                        }
                        i++;
                      }
                      if (numero(exp[i+1]) || trigon(exp[i+1]) || 
                          punto(exp[i+1]) || valorAbs(exp[i+1]) || 
                          !exp[i] || parAbierto(exp[i+1])){
                            return false;
                      } 
                    } else {
                        return false;
                      }
                  } else {
                    if (operador(exp[i])){
                      if (operador(exp[i+1]) || parCerrado(exp[i+1]) || !exp[i+1] || (!exp[i-1] && exp[i]!='-')){
                        return false;
                      } else {
                        if (parCerrado(exp[i])){
                          parentesis--;
                          cout << "{ver 3} total parentesis: "<< parentesis << endl;
                          if (parCerrado(exp[i+1]) || numero(exp[i+1]) || trigon(exp[i+1]) || valorAbs(exp[i+1])){
                            return false;
                          } else {
                            if (valorAbs(exp[i])){
                              i=i+1;
                              if (valorAbs(exp[i])){
                                return false;
                              }
                              if (exp[i]==('-')){
                                i++;
                              }
                              int valorPunto = 0;
                              while (exp[i] && !valorAbs(exp[i])){
                                if (punto(exp[i])){
                                  valorPunto++;
                                }
                                if (!numero(exp[i]) && !punto(exp[i]) && valorPunto>1){
                                  return false;
                                }
                                i++;
                              }
                            
                              if (!exp[i] || valorAbs(exp[i+1]) || punto(exp[i+1]) || numero(exp[i+1]) || trigon(exp[i+1]) || parAbierto(exp[i+1])){
                                return false;
                              }
                          } else {
                            if (punto(exp[i])){
                              if (!numero(exp[i+1])){
                                return false;
                              }
                            } else {
                              return false;
                            }
                          }
                        }
                      }
                    }
                  }
               }
              }
            }     
      if (parCerrado(exp[i])){
                          parentesis--;
                          cout << "{ver 3} total parentesis: "<< parentesis << endl;
      } 
     }

    i++;
    }
    if (parentesis!=0){
        return false;
      }
    return true;
 }
  

bool Verificador::operador(char caracter){
    switch (caracter)
    {
      case '+':
        return true;
      case '-':
        return true;
      case '*':
        return true;
      case '/':
        return true;
      default:
        return false;
    }
}

bool Verificador::numero(char caracter){
    switch (caracter)
    {
      case '0':
        return true;
      case '1':
        return true;
      case '2':
        return true;
      case '3':
        return true;
      case '4':
        return true;
      case '5':
        return true;
      case '6':
        return true;
      case '7':
        return true;
      case '8':
        return true;
      case '9':
        return true;
    }
    return false;
}


bool Verificador::parAbierto(char caracter){
    if (caracter=='('){
        return true;
    }
    return false;
}

bool Verificador::parCerrado(char caracter){
    if (caracter==')'){
        return true;
    }
    return false;
}

bool Verificador::trigon(char letra){
  switch (letra){
    case 'c': return true;
      break;
    case 't': return true;
      break;
    case 's': return true;
      break;
    default: return false;
      break;
  }
}

bool Verificador::trigonometrica(string trig){
  if (trig.compare("sen(")!=0 && trig.compare("cos(")!=0 && trig.compare("tan(")!=0){
    return false;
  } else {
    return true;
  }
}

bool Verificador::valorAbs(char valor){
  if (valor=='|'){
    return true;
  } else {
    return false;
  }
}

bool Verificador::punto(char caracter){
    if(caracter=='.'){
        return true;
    }
    return false;
}

string Verificador::quitarEspacio(string exp){
    string expNueva = "";
    int i=0;
    while(exp[i]){
        if (exp[i]!= ' '){
            expNueva+=exp[i];
        }
        i++;
    }
    cout << exp << "::" << expNueva << endl;
    return expNueva;
}
