// Queen's Love of my life melody for a passive buzzer

#include "pitches.h"

int melody[] = {
  NOTE_C5, NOTE_B4, NOTE_C5, NOTE_G5, REST,
  NOTE_B4, NOTE_B4, NOTE_A4, REST,
  NOTE_A4, NOTE_F5, NOTE_E5, NOTE_F5, NOTE_A5, REST,
  NOTE_A4, NOTE_G4, NOTE_G5, NOTE_G5, NOTE_F5,
  NOTE_E5, NOTE_D5, NOTE_C5, NOTE_A5, 
  NOTE_G5, NOTE_A5, NOTE_A5
};

// Note durations: 4 = quarter note, 8 = eighth note
int noteDurations[] = {
  // Love of my life
  4, 4, 4, 1.5, 2.5,
  // You've hurt me
  4, 2, 1.5, 2.5,
  // You've broken my heart
  4, 4, 4, 4, 1.5, 2.5,
  // And now you leave me
  2, 2, 2, 2, 2,
  // Love of my life
  4, 4, 4, 2.5,
  // Can't you see
  2, 4, 1
};

const int buzzerPin = 8; 

void setup() {
  // Iterate over the notes of the melody:
  int size = sizeof(melody) / sizeof(int);
  for (int thisNote = 0; thisNote < size; thisNote++) {

    // Calculating note duration
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(buzzerPin, melody[thisNote], noteDuration);

    // Pause between notes
    int pauseBetweenNotes = noteDuration * 1.3;
    delay(pauseBetweenNotes);
    
    // Stop the tone playing:
    noTone(buzzerPin);
  }
}

void loop() {
}
