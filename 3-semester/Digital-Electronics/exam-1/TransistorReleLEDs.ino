#define RELAY 49
#define PIN 22

void setup() {
  pinMode(PIN, INPUT);
  pinMode(RELAY, OUTPUT);
}

void loop() {
  digitalWrite(RELAY, digitalRead(PIN));
}