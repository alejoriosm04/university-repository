#pragma once
#include <iostream>
#include <string>
#include "Data.h"

using namespace std;

class Dictionary {
    private:
        Data* data;
        string key;
        Dictionary* head;

    public:
        Dictionary* next;
        Dictionary(){
            this->head = NULL;
        }
        Dictionary(string key, Data* data);
        void add(string key, Data* data);
        // Data* get(string key);
        void get(string key);
        void printData();
        void show();
};