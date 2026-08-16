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

### LCD Pin Connection

The Arduino sketch initializes the display using `LiquidCrystal lcd(7, 8, 9, 10, 11, 12)`:

| LCD Pin | Description | Arduino / Circuit Connection |
|---|---|---|
| **VSS** | Ground | Arduino `GND` |
| **VDD** | Power (+5V) | Arduino `5V` |
| **V0** | Contrast control | Potentiometer wiper (center pin) |
| **RS** | Register Select | Arduino Digital Pin `7` |
| **RW** | Read/Write | Arduino `GND` |
| **E** | Enable | Arduino Digital Pin `8` |
| **D4** | Data Bit 4 | Arduino Digital Pin `9` |
| **D5** | Data Bit 5 | Arduino Digital Pin `10` |
| **D6** | Data Bit 6 | Arduino Digital Pin `11` |
| **D7** | Data Bit 7 | Arduino Digital Pin `12` |
| **A (LED+)** | Backlight Anode | `5V` (via 220Ω resistor) |
| **K (LED-)** | Backlight Cathode | Arduino `GND` |

---

## Software & Dependencies

- **macOS** (uses `osascript` to communicate with the Music/Musiikki app)
- **Python 3**
- **pyserial** package:
  ```bash
  pip install pyserial
  ```
- **Arduino IDE** (with the built-in `LiquidCrystal` library)

---

## File Structure

- `apple_music_scripts.py` – AppleScript wrapper functions to start playback and query the current track position.
- `lyric_display.py` – Main Python script for `.lrc` parsing, time tracking, and serial communication.
- `lyric_display.ino/` – Arduino sketch to receive serial messages and print them to the LCD.
- `wicked_game.lrc` – Example timestamped LRC lyric file (Chris Isaak – *Wicked Game*).

---

## Setup & Usage

1. **Upload the Arduino Sketch**:
   - Open `lyric_display.ino/lyric_display.ino.ino` in the Arduino IDE.
   - Select your board and port, then click **Upload**.

2. **Configure the Python Script**:
   - In `lyric_display.py`, verify/update `ARDUINO_PORT` with your Arduino's serial port (e.g., `/dev/cu.usbmodem1201`):
     ```python
     ARDUINO_PORT = "/dev/cu.usbmodem1201"
     ```
   - In `apple_music_scripts.py`, check that the playlist name and track name match your Apple Music library (default: playlist `"rokkia ja muuta"`, track `"Wicked Game"`).

3. **Run the Script**:
   ```bash
   python3 lyric_display.py
   ```
   The script will start playback in Apple Music and display synchronized lyrics on the LCD screen.
