/*
  Code to execute a traffic light in Arduino that blinks the green light 3 times before turning it to red again
*/

#define RED 24
#define YELLOW 23
#define GREEN 22
int tinicial = 0;
int tfinal = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(RED, HIGH);
  delay(5000);
  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, HIGH);
  delay(1000);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, HIGH);
  delay(2000);
  digitalWrite(GREEN, LOW);
  
  delay(500);
  digitalWrite(GREEN, HIGH);
  delay(500);
  digitalWrite(GREEN, LOW);
  delay(500);
  digitalWrite(GREEN, HIGH);
  delay(500);
  digitalWrite(GREEN, LOW);
  delay(500);
  digitalWrite(GREEN, HIGH);
  delay(500);
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, HIGH);
  delay(1000);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, HIGH);
  delay(1000);
  digitalWrite(RED, LOW);

}