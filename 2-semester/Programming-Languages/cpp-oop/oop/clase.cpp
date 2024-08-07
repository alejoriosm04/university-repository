#include <iostream>
using namespace std;

class Clase {
  //private
  private:
    int valor1;
    int valor2;

  //public
  public:
    Clase(int valor1, int valor2); //constructor
    ~Clase(){
		cout<<"Me destruyen..."<<endl;
	}; //destructor
    int getValor1();
    int getValor2();
    void setValor1(int valor1);
    void setValor2(int valor2);

  //protected
  //protected:
};


Clase::Clase(int valor1, int valor2){
	this->valor1 = valor1;
	this->valor2 = valor2;
}

int Clase::getValor1(){
	return this->valor1;
}
int Clase::getValor2(){
	return this->valor2;
}
void Clase::setValor1(int valor){
	this->valor1 = valor;
}
void Clase::setValor2(int valor){
	this->valor2 = valor;
}

//===========================================

int main(){
	int x = 3;
	int y = 6;

	Clase *obj1 = new Clase(x,y);
	cout << "Valor 1 = " << obj1->getValor1() << endl;
	cout << "Valor 2 = " << obj1->getValor2() << endl;
	
	return 0;
}