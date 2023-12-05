/*
  Code to execute a traffic light in Arduino that turns red when the user presses a button
*/

#define RED 24
#define YELLOW 23
#define GREEN 22
#define PERSON 37
int tinicial = 0;
int tfinal = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(PERSON, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(GREEN, HIGH);
  tinicial = millis();
  tfinal = millis();
  while(tfinal - tinicial < 10000 && digitalRead(PERSON) == LOW){
    tfinal = millis();
  }
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
  delay(500);

  digitalWrite(YELLOW, HIGH);
  delay(1000);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, HIGH);
  delay(1000);
  digitalWrite(RED, LOW);

}