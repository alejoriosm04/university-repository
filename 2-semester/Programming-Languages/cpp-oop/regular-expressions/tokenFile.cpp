#include <iostream>
#include <string>
#include <fstream>
#include <string.h>

using namespace std;

void writeFile(string fileName, string info){
    // Create output file
    ofstream outputFile(fileName);

    // Send info to disc memory
    outputFile << info << endl;

    // Close file
    outputFile.close();

}

string readFile(string fileName){
    string info = "";
    
    // Open file
    ifstream inputFile(fileName);

    // Read file
    int i = 0;
    while(!inputFile.eof()){
        string line;
        i++;
        getline(inputFile, line, '\n');
        info += "Linea[" + to_string(i) + "] " + line + "\n";
    }

    // Close file
    inputFile.close();
    return info;
}

int main(int argc, char* argv[]){
    if (strcmp(argv[1], "-h") == 0){
        cout << "Lenguaje de Programación Edi++ Versión 0.0 (2022)" << endl;
    } else {
        string fileName = argv[1];

        // writeFile("jedi.txt", "Hola a todos; Estoy feliz; Adios");
        cout << readFile(fileName) << endl;
    }

    /*
    string fileName = argv[1];
    
    // writeFile("jedi.txt", "Hola a todos; Estoy feliz; Adios"); 
    cout << readFile(fileName) << endl;
    // */

    return 0;
}
