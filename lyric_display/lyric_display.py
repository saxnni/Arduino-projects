
import time
import re
import serial
import apple_music_scripts

ARDUINO_PORT = "/dev/cu.usbmodem1101"
BAUD_RATE = 9600


def parse_lrc(file_path):
    lyrics = []

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\[(\d+):(\d+\.\d+)\](.*)", line)
            if m:
                minutes = int(m.group(1))
                seconds = float(m.group(2))
                text = m.group(3).strip()

                time_sec = minutes * 60 + seconds

                lyrics.append((time_sec, text))

    return lyrics


def find_current_lyric(lyrics, position):
    if position is None or not lyrics:
            return ""

    position = float(str(position).replace(",", "."))

    current_text = ""
    for sec, text in lyrics:
        if sec <= position:
            current_text = text
        else:
            break

    return current_text


def send_to_arduino(ser, text):
    if ser and ser.is_open:
        ser.write((text + "\n").encode("utf-8"))


def main():
    apple_music_scripts.play_song()

    lyrics = parse_lrc("wicked_game.lrc")

    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)

    last_sent = ""

    while True:
        pos = apple_music_scripts.get_position()
        current_lyric = find_current_lyric(lyrics, pos)

        if current_lyric and current_lyric != last_sent:
            print(f"[{pos}s] Uusi rivi: {current_lyric}")
            send_to_arduino(ser, current_lyric)
            last_sent = current_lyric

        time.sleep(0.3)  


if __name__ == "__main__":
    main()