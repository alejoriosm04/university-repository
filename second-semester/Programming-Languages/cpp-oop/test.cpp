// A Polish Notation Calculator with Stack behavior

#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cmath>

using namespace std;

// Function to check if a string is a number
bool isNumber(string s) {
    for (int i = 0; i < s.length(); i++)
        if (isdigit(s[i]) == false)
            return false;
    return true;
}

// Function to check if a string is an operator
bool isOperator(string s) {
    if (s == "+" || s == "-" || s == "*" || s == "/" || s == "^")
        return true;
    return false;
}

// Function to check if a string is a function
bool isFunction(string s) {
    if (s == "sqrt" || s == "sin" || s == "cos" || s == "tan")
        return true;
    return false;
}

// Function to check if a string is a variable
bool isVariable(string s) {
    if (s == "x" || s == "y" || s == "z")
        return true;
    return false;
}


// Function to convert a string to a number
double toNumber(string s) {
    double d;
    stringstream ss(s);
    ss >> d;
    return d;
}


// Function to convert a string to a function
double toFunction(string s, double x) {
    if (s == "sqrt")
        return sqrt(x);
    else if (s == "sin")
        return sin(x);
    else if (s == "cos")
        return cos(x);
    else if (s == "tan")
        return tan(x);
    else
        return 0;
}

// Function to convert a string to a variable
double toVariable(string s, double x, double y, double z) {
    if (s == "x")
        return x;
    else if (s == "y")
        return y;
    else if (s == "z")
        return z;
    else
        return 0;
}

// Function to convert a string to an operator
double toOperator(string s, double x, double y) {
    if (s == "+")
        return x + y;
    else if (s == "-")
        return x - y;
    else if (s == "*")
        return x * y;
    else if (s == "/")
        return x / y;
    else if (s == "^")
        return pow(x, y);
    else
        return 0;
}


// Function to convert a string to a vector of strings
vector<string> toVector(string s) {
    vector<string> v;
    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ')
            continue;
        else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || s[i] == '^') {
            if (temp != "")
                v.push_back(temp);
            temp = "";
            temp += s[i];
            v.push_back(temp);
            temp = "";
        }
        else if (s[i] == '(' || s[i] == ')') {
            if (temp != "")
                v.push_back(temp);
            temp = "";
            temp += s[i];
            v.push_back(temp);
            temp = "";
        }
        else if (s[i] == 's' || s[i] == 'c' || s[i] == 't') {
            if (temp != "")
                v.push_back(temp);
            temp = "";
            temp += s[i];
            i++;
            temp += s[i];
            i++;
            temp += s[i];
            v.push_back(temp);
            temp = "";
        }
        else if (s[i] == 'x' || s[i] == 'y' || s[i] == 'z') {
            if (temp != "")
                v.push_back(temp);
            temp = "";
            temp += s[i];
            v.push_back(temp);
            temp = "";
        }
        else {
            temp += s[i];
        }
    }
    if (temp != "")
        v.push_back(temp);
    return v;
}