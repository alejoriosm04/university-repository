#include <iostream>
#include <string>
#include "Paises.h"

using namespace std;

int main() {
    Pais* objP1 = new Pais("Colombia", "Bogotá", 51049000);
    cout << objP1 -> verDatos() << endl;
    return 0;
}