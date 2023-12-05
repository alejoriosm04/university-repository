int botonPin = 19;
int contador = 0;

void setup() {
  pinMode(botonPin, INPUT); 
  attachInterrupt(4, incrementarContador, FALLING);
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
