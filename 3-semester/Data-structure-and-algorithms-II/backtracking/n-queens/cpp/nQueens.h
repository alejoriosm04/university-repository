#pragma once
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class nQueens {
    private:
        int N;
        int solution;
        vector<vector<int> > board;
    
    public:
        nQueens(int N);
        ~nQueens();
        void setQueens(int row);
        bool validate(int row, int col);
        void printBoard();
    
};