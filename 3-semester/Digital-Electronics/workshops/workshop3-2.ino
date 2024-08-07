#define IN_AN0 A0
#define PMW_Pin 9

// Segementos del display
int segmentos[7] = { 29, 28, 27, 26, 25, 24, 23 };
// Unidades y decenas
int num[2] = { 0, 0 };
int unid = 30;
int dec = 31;

//Subroutines and functions

void setup() {

  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
  }
  pinMode(unid, OUTPUT);
  pinMode(dec, OUTPUT);
  pinMode(IN_AN0, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Add a delay 500 milliseconds
  delay(500);
  int valor = analogRead(IN_AN0);
  valor = map(valor, 0, 1023, 0, 255);
  analogWrite(PMW_Pin, valor);
  int valor2 = map(analogRead(IN_AN0), 0, 1023, 0, 99);
  display((valor2 % 10), unid);
  display((valor2 / 10), dec);
  // put your main code here, to run repeatedly:
}


void display(int value, int module) {
  //a  b  c  d  e  f  g
  int num[10][7] = { 1, 1, 1, 1, 1, 1, 0,
                     0, 1, 1, 0, 0, 0, 0,
                     1, 1, 0, 1, 1, 0, 1,
                     1, 1, 1, 1, 0, 0, 1,
                     0, 1, 1, 0, 0, 1, 1,
                     1, 0, 1, 1, 0, 1, 1,
                     1, 0, 1, 1, 1, 1, 1,
                     1, 1, 1, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 0, 0, 1, 1 };

  for (int k = 0; k < 7; k++) {
    digitalWrite(segmentos[k], num[value][k]);
  }
  digitalWrite(module, HIGH);
  delay(5);
  digitalWrite(module, LOW);
}