import time
import random
import serial

# Laitetaan active buzzer piippaamaan, kun "räjähdys" tapahtuu

arduino = serial.Serial("/dev/cu.usbmodem1101", 9600)
time.sleep(2)

def ArvoVastaus():

    vastaus = [
        "Broidi mä vannon mitään pahaa ei tapahu!",
        "Älä pelkää :))))))",
        "Usko nyt.",
        "Huoh...",
        "Älä pelleile.",
        "Etkö sä luota muhun :0"
        "Pweeease"
    ]

    indeksi = random.randint(0, 4)

    return vastaus[indeksi]

inp = input("Syötä q... ")

while (inp.find("q") == -1):
    text = ArvoVastaus()
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)
        
    print()

    inp = input("Syötä q... ")

text4 = "Ootko varma? \n"
for char in text4:
    print(char, end="", flush=True)
    time.sleep(0.1)

time.sleep(0.4)

text5 = "Ähäkutti \n"

for char in text5:
    print(char, end="", flush=True)
    time.sleep(0.1)

arduino.write(b'B')
for x in reversed(range(1,11)):
    print(x)
    time.sleep(0.5)

text2 = "K A B O O M ! ! ! 💣 💣 💣"
for char in text2:
    print(char, end="", flush=True)
    time.sleep(0.1)

print()

text3 ="Räjähdit. \nSori siitä :( \n"
for char in text3:
    print(char, end="", flush=True)
    time.sleep(0.1)
