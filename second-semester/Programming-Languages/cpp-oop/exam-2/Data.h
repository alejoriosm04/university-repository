#pragma once
#include <iostream>
#include <string>

using namespace std;

class Data {
    private:
        string brand;
        string model;

    public:
        Data(string brand, string model);
        Data();
        string seeData();

};