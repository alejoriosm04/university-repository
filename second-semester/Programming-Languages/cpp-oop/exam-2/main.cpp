#include <iostream>
#include <string>
#include "Data.h"
#include "Dictionary.h"

using namespace std;

int main(){
    Dictionary* transport_means = new Dictionary();

    // Testing with means of transport
    transport_means->add("Auto", new Data("Mercedes Benz", "C180"));
    transport_means->add("Motocicleta", new Data("BMW", "R 1250 GS"));
    transport_means->add("Auto", new Data("Chevrolet", "Camaro SS"));
    transport_means->add("Avion", new Data("Boeing", "787-DreamLiner"));
    transport_means->add("Auto", new Data("Volskwagen", "Golf GTI"));
    transport_means->add("Avion", new Data("Airbus", "A350-700"));
    cout << "---------------" << endl;

    // Printing all data with show() method.
    transport_means->show();

    cout << "---------------" << endl;

    // Search with a specific key to find.
    string search = "Avion";
    cout << "Search: " << search << endl;
    transport_means->get(search);

    return 0;
}