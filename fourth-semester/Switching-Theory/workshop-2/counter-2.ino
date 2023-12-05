#include <TimerOne.h>
int botonPin = 19;
int contador = 0;

void setup() {
  Timer1.initialize(1000000);
  pinMode(botonPin, INPUT); 
  Timer1.attachInterrupt(incrementarContador);
  Serial.begin(9600);
}

void loop() {
  
}

void incrementarContador() {
  contador++;
  Serial.print("Contador: ");
  Serial.println(contador); 
}