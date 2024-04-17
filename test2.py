from pydub import AudioSegment
import numpy as np
import soundfile as sf
from scamp import *
import time
import serial

ser = serial.Serial('COM26', 115200, timeout=0)

def get_bpm():
    for i in m:
        if i != "":
            print(i)
            while True:
                if int(i) < 120 and int(i) > 0:
                    print(i)
                    return i
import time  # Importing the time module for the sleep function

def get_pressure():
    count = 0
    values = []
    for i in m:
        if i != "":
            try:
                i = int(i)  # Convert i to an integer
            except ValueError:
                # Handle the case where i cannot be converted to an integer
                continue
            while True:
                if i > 120:
                    i /= 100  # Convert i to the appropriate pressure value
                    values.append(i)
                    count += 1
                    time.sleep(0.1)
                if count >= 10:
                    return values

def get_stuff():
    values = []
    count = 0
    data = ser.readline().strip()
    while True:
        if data and b':' in data:
            name,value = data.decode().split(':')
            if value:
                try:
                    if name == 'pressure':
                        pressure = int(value)
                        print('Presure', pressure)
                        count += 1

                    elif name == 'heart':
                        heart = int(value)
                        tempo = heart
                        count+= 1
                        values.append(heart)
                        break
                    elif count == 21:
                        return tempo, values

                except ValueError:
                    print('error')
                    countinue
    time.sleep(0.1)
    
session = Session()

bpm , pitches = get_stuff()

if bpm > 90:
    bpm = 120

elif bpm < 70:
    bpm = 30

piano1 = session.new_part("Piano")
piano2 = session.new_part("Guitar")

for pitch in pitches:
    if pitch < 10:
        pitch = pitch * 8
        if pitch < 2:
            pitch = 15
    if pitch > 90:
        pitch = pitch * 0.96
print(pitches)
# pitches = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]


def piano_part(which_piano):
    while True:
        for pitch in pitches:
            which_piano.play_note(pitch, 1.0, 0.25)

clock1 = session.fork(piano_part, args=(piano1,), initial_tempo=bpm)
clock2 = session.fork(piano_part, args=(piano2,), initial_tempo=bpm-5)

session.start_transcribing(clock=clock1)
session.wait(10)

performance = session.stop_transcribing()