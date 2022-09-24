#include <iostream>
#include <string>
#include "Data.h"

using namespace std;

Data::Data(string brand, string model){
    this->brand = brand;
    this->model = model;
}

Data::Data(){
    this->brand = "Sin marca";
    this->model = "Sin modelo";
}

string Data::seeData(){
    string valor = "Brand: ";
    valor = valor + this->brand + " - (Model: " + this->model + ")";
    return valor;
}