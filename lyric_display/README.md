# Lyric Display

Synchronize and display real-time song lyrics on a 16x2 LCD display connected to an Arduino while playing music through Apple Music on macOS.

## How It Works

1. **AppleScript Integration (`apple_music_scripts.py`)**: Controls macOS Apple Music (Musiikki) to play a designated track and continuously polls the current playback position in seconds.
2. **Lyric Parser & Serial Transmitter (`lyric_display.py`)**: Parses standard `.lrc` timestamped lyric files, matches the current song position to the corresponding lyric line, and sends new lines over the USB serial port to the Arduino.
3. **Arduino LCD Controller (`lyric_display.ino`)**: Receives the lyric text over serial and renders it on a 16x2 LCD screen, wrapping lines longer than 16 characters across both rows.

---

## Hardware Requirements

- **Arduino Board** (e.g., Arduino UNO R3)
- **16x2 Character LCD** (HD44780 compatible)
- **10kΩ Potentiometer** (for LCD contrast adjustment) or fixed resistor
- **Breadboard & Jumper Wires**
- **USB Cable** (connecting Arduino to Mac)



