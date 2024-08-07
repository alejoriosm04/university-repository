#include <TimerOne.h>

int botonPinInc = 19;
int botonPinDec = 18;
int botonPinStart = 20;
int botonPinReset = 21;
int contador = 0;

void setup() {
  pinMode(botonPinInc, INPUT); 
  pinMode(botonPinDec, INPUT); 
  pinMode(botonPinStart, INPUT); 
  pinMode(botonPinReset, INPUT); 
  Timer1.initialize(1000000);
  attachInterrupt(4, incrementarContador, FALLING);
  attachInterrupt(5, decrementarContador, FALLING);
  attachInterrupt(3, cronometro, FALLING);
  Serial.begin(9600);
}

void loop() {
  
}

void incrementarContador() {
  detachInterrupt(4);
  contador++;
  Serial.print("Contador: ");
  Serial.println(contador);
  attachInterrupt(4, incrementarContador, FALLING);
}

void decrementarContador() {
  detachInterrupt(4);
  if (contador != 0) {
    contador--;
  }
  Serial.print("Contador: ");
  Serial.println(contador);
  attachInterrupt(4, incrementarContador, FALLING);
}

void cronometro() {
  if (contador != 0) {
    contador--;
    Timer1.attachInterrupt(cronometro);
    attachInterrupt(2, reset, FALLING);
  }
  else {
    Timer1.detachInterrupt();
    detachInterrupt(2);
  }
  Serial.print("Contador: ");
  Serial.println(contador);
}

void reset() {
  contador = 0;
  Serial.println("Contador reiniciado.");
}