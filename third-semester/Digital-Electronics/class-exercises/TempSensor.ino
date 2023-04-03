#define temp A0

void setup() {
  // put your setup code here, to run once:
  pinMode(temp, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float value = ((analogRead(temp)*3.3)/1023.0)*100;
  Serial.println(value);
  delay(500);
}