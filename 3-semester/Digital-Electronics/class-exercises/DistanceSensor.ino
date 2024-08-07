//I/O Pin Labeling
#define ECHO 23 //Ultrasonic ECHO pin connected to Arduino pin 2
#define TRIG 22 //Ultrasonic TRIG pin connected t Arduino pin 3
//Variable declaration
unsigned int distance = 0;  //Variable for storing the value of the (distance)
//Subroutines and functions
unsigned int ultraMeas(unsigned int ECHOPIN, unsigned int TRIGPIN) {
  delay(50);  //Delay of 50 ms before the next ranging
  digitalWrite(TRIGPIN, HIGH); //Turn ON the TRIG for measuring the distance
  delayMicroseconds(10);  //Wait 10uSecs with the TRIG ON
  digitalWrite(TRIGPIN, LOW); //Turn OFF the TRIG
  return pulseIn(ECHOPIN, HIGH)/58.0; //Return the distance on centimeters
}

void setup() {
  //I/O Pin Definition
  pinMode(ECHO, INPUT); //ECHO Pin as input
  pinMode(TRIG, OUTPUT);  //TRIG Pin as output
  //Physical Output Cleaning
  digitalWrite(TRIG, LOW);
  //Communications
  Serial.begin(9600); 
}
  void loop() {
  distance = ultraMeas(ECHO, TRIG);  //Measure distance
  Serial.print("Distance (cm): ");
  Serial.println(distance);
}