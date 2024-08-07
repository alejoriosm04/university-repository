#define LEFT 22
#define RIGHT 23
#define RELAY 49

void setup() {
  // put your setup code here, to run once:
  pinMode(LEFT, RIGHT);
  pinMode(RIGHT, OUTPUT);
  pinMode(RELAY, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEFT, LOW);
  digitalWrite(RIGHT, LOW);
  delay(100);

  digitalWrite(LEFT, HIGH);
  digitalWrite(RIGHT, LOW);
  digitalWrite(RELAY, HIGH);
  delay(100);

  digitalWrite(LEFT, LOW);
  digitalWrite(RIGHT, LOW);
  digitalWrite(RELAY, LOW);
  delay(100);

  digitalWrite(LEFT, HIGH);
  digitalWrite(RIGHT, LOW);
  digitalWrite(RELAY, HIGH);
  delay(100);
}
