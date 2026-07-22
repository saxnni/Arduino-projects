#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  if (Serial.available() > 0) {
    String text = Serial.readStringUntil('\n');
    text.trim();

    lcd.clear();

    if (text.length() > 16) {
      lcd.setCursor(0, 0);
      lcd.print(text.substring(0, 16)); 
      
      lcd.setCursor(0, 1);
      lcd.print(text.substring(16, 32));
    } else {
      lcd.setCursor(0, 0);
      lcd.print(text);
    }
  }
}
