#include <iostream>
#include <vector>
using namespace std;

const int N = 8;

vector<vector<int> > tablero(N, vector<int>(N));

int solucion = 0;

//Find the 92 solutions

// static bool ponerReina(int fila) {
//     if(fila == N) {
//         solucion++;
//         cout << "Solucion: " << solucion << endl;
//         imprimirTablero();
//         return true;
//     }
    
//     for(int col = 0; col < N; col++) {
//         if(validar(fila, col)) {
//             tablero[fila][col] = 1;
//             if(ponerReina(fila + 1)) {
//                 return true;
//             }
//             tablero[fila][col] = 0;
//         }
//     }

//     return false;
// }

bool validar(int fila, int col) {
    // Validar la columna
    for(int f = 0; f < fila; f++) {
        if(tablero[f][col] == 1) return false;
    }
    
    // Validar diagonal 1
    int f = fila - 1; int c = col - 1;
    while(f >= 0 && c >= 0) {
        if(tablero[f][c] == 1) return false;
        f--;
        c--;
    }
    // Validar diagonal 2
    f = fila - 1; c = col + 1;
    while(f >= 0 && c < N) {
        if(tablero[f][c] == 1) return false;
        f--;
        c++;
    }
    return true;
}

void imprimirTablero() {
    for(int fila = 0; fila < N; fila++) {
        for(int col = 0; col < N; col++) {
            cout << tablero[fila][col] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void ponerReina(int fila) {
    if(fila == N) {
        solucion++;
        cout << "Solucion: " << solucion << endl;
        imprimirTablero();
        return;
    }
    
    for(int col = 0; col < N; col++) {
        if(validar(fila, col)) {
            tablero[fila][col] = 1;
            ponerReina(fila + 1);
            tablero[fila][col] = 0;
        }
    }
}

int main() {
    imprimirTablero();
    ponerReina(0);
}