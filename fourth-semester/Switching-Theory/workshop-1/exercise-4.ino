/*
    Code to get a random numer with a seed and millis
    in the Serial Monitor
*/

#define BUTTON_PIN 37 // Define the pin where the button is connected

void setup() {
  pinMode(BUTTON_PIN, INPUT; // Set the button pin as input with a pull-up resistor
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW) { // Check if the button is pressed
    randomSeed(seed);
    
    // Generate a random number based on the current time (millis())
    int randomNumber = random(0, 100); // Change the range as needed
    
    Serial.print("Random Number: ");
    Serial.println(randomNumber);
    
    // Delay a bit to avoid multiple readings from a single button press
    delay(500);
  }
}
