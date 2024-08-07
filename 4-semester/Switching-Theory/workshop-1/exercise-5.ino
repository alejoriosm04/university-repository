/*
    Game to guess if a random number is greater, equal or less than 5
    with levels and time limit of 10 seconds
*/

#define START 37
#define LESS 36
#define EQUAL 35
#define GREATER 34
int resultado = 0;
int nivel = 1;

void setup() {
  pinMode(START, INPUT);
  pinMode(LESS, INPUT);
  pinMode(EQUAL, INPUT);
  pinMode(GREATER, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(START) == HIGH) {
    Serial.println("Juego iniciado");
    int numero = random(0, 10);
    Serial.println(nivel);
    Serial.println("Numero generado");
    Serial.println("Adivina si es mayor, igual o menor a 5");
    Serial.println("Tienes 10 segundos");
    int tiempo = millis();
    int respuesta = -1; // Initialize respuesta with an invalid value
    bool flag = true;
    bool timeout = false; // Initialize timeout flag
    
    while (flag && !timeout) {
      if (millis() - tiempo >= 10000) {
        Serial.println("Tiempo agotado, no se proporcionó una respuesta.");
        timeout = true;
      }
      
      if (digitalRead(LESS) == HIGH && digitalRead(EQUAL) == LOW && digitalRead(GREATER) == LOW) {
        respuesta = 0; // Less than 5
      } else if (digitalRead(EQUAL) == HIGH && digitalRead(LESS) == LOW && digitalRead(GREATER) == LOW) {
        respuesta = 1; // Equal to 5
      } else if (digitalRead(GREATER) == HIGH && digitalRead(LESS) == LOW && digitalRead(EQUAL) == LOW) {
        respuesta = 2; // Greater than 5
      }
      
      if (respuesta != -1) {
        if (timeout) {
          // If there was a timeout, don't evaluate the answer
          Serial.println("Tiempo agotado, no se proporcionó una respuesta.");
          resultado = 0;
        } else {
          if ((respuesta == 0 && numero < 5) || (respuesta == 1 && numero == 5) || (respuesta == 2 && numero > 5)) {
            Serial.println("Ganaste");
            resultado = 1;
          } else {
            Serial.println("Perdiste");
            resultado = 0;
          }
        }
        
        if (resultado == 0) {
          Serial.println("Juego terminado");
        } else {
          nivel = nivel + 1;
        }
        
        Serial.println(numero);
        delay(1000);
        flag = false; // Exit the loop after evaluating the answer
      }
    }
  }
}
