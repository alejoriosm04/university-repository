// This code is for the RGB LED circuit

// Indicate ports or pines of Arduino
int Analog = A0;
#define Red 8;
#define Green 7;
#define Blue 6;

void setup() {
		// Assign INPUTS and OUTPUTS
    pinMode(Analog, INPUT);
    pinMode(Red, OUTPUT);
    pinMode(Green, OUTPUT);
    pinMode(Blue, OUTPUT);
    Serial.begin(9600);
}


void loop() {
		// Save sensor value in a variable
    int sensorValue = analogRead(Analog);
    Serial.println((sensorValue * 5) / 1023.0); // Print values in serial monitor
    delay(100);
	// Send sensor values to each color
    analogWrite(Red, sensorValue); 
    analogWrite(Green, sensorValue);
    analogWrite(Blue, sensorValue);
}