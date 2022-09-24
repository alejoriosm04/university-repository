#include <iostream>
#include <string>
#include "Dictionary.h"

using namespace std;

Dictionary::Dictionary(string key, Data* data){
    this->key = key;
    this->data = data;
    this->next = NULL;
}

void Dictionary::add(string key, Data* data){
    Dictionary* node = new Dictionary(key, data);
    if (this->head ==  NULL) {
        this->head = node;
        node->next = NULL;
    } else {
        Dictionary* aux = this->head;
        while (aux->next != NULL) {
            aux = aux->next;
        }
        aux->next = node;
        node->next = NULL;
    }
}

// I wasn't able to create this method with a Data* return.....

// Data* Dictionary::get(string key){
//     Dictionary* aux = this->head;
//     Data* aux_data = new Data();
//     while (aux != NULL) {
//         if (aux->key == key) {
//             aux_data = aux->data;
//         }
//         aux = aux->next;
//     }
//     return aux_data;
// }

void Dictionary::get(string key){
    cout << "---------------" << endl;
    Dictionary* aux = this->head;
    while (aux != NULL) {
        if (aux->key == key) {
            cout << aux->data->seeData() << endl;
        }
        aux = aux->next;
    }
    cout << "---------------" << endl;
}

void Dictionary::show(){
    Dictionary* aux = this->head;
    while (aux != NULL) {
        aux->printData();
        aux = aux->next;
    }
}

void Dictionary::printData(){
    cout << "{  [" << this->key << "]->" << this->data->seeData() << "  }->" << endl;
}