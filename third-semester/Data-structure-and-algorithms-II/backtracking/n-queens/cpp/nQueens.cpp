#include <iostream>
#include <string>
#include "nQueens.h"
#include <vector>

using namespace std;

nQueens::nQueens(int N){
    this->N = N;
    this->board = vector<vector<int> >(N, vector<int>(N));
    //fill the board with 0
    for(int row = 0; row < N; row++){
        for(int col = 0; col < N; col++){
            this->board[row][col] = 0;
        }
    }
    this->solution = 0;
}

void nQueens::setQueens(int row){
    if(row == this->N) {
        this->solution++;
        cout << "Solution " + this->solution << endl;
        printBoard();
        return;
    }

    for(int col = 0; col < N; col++){
        if(validate(row, col)){
            this->board[row][col] = 1;
            setQueens(row+1);
            this->board[row][col] = 0;
        }
    }
}

bool nQueens::validate(int row, int col){
    // Validate row
    for(int r = 0; r < row; r++){
        if(this->board[r][col] == 1){
            return false;
        }
    }

    // Validate diagonal 1
    int r = row - 1; int c = col - 1;
    while(r >= 0 && c >= 0) {
        if(this->board[r][c] == 1){
            return false;
        }
        r--;
        c--;
    }

    // Validate diagonal 2
    r = row - 1; c = col + 1;
    while(r >= 0 && c >= 0) {
        if(this->board[r][c] == 1){
            return false;
        }
        r--;
        c++;
    }
    return true;
}

void nQueens::printBoard(){
    for(int row = 0; row < N; row++){
        for(int col = 0; col < N; col++){
            cout << this->board[row][col] + " ";
        }
        cout << endl;
    }
    cout << endl;
}

int main(){
    nQueens* chessBoard1 = new nQueens(8);
    chessBoard1->printBoard();
    chessBoard1->setQueens(0);
}
