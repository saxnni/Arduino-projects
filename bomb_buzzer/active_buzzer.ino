// Pin of the active buzzer
int buzzer = 12;
void setup() {
  // initialize the buzzer pin as an output
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Waits for a message from Python
  if (Serial.available()) {

    char c = Serial.read();

    if (c == 'B') {
      // 10 short beeps
      for (int i = 0; i < 10; i++) {

        digitalWrite(buzzer, HIGH);
        delay(250);

        digitalWrite(buzzer, LOW);
        delay(250);
      }

      delay(300);

      // 5 s long beep
      digitalWrite(buzzer, HIGH);
      delay(5000);

      digitalWrite(buzzer, LOW);

      while(true);
    }
  }
}
