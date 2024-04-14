from pydub import AudioSegment
import numpy as np
import soundfile as sf
from scamp import *
from microserial import Microbit
import random

# m=Microbit()

def get_bpm():
    return random.randint(50,90)
    
def get_pressure():
    list = []
    for i in range(10):
        list.append(random.randint(1,100))
    return list


session = Session()

bpm = get_bpm()
bpm = int(bpm)
# bpm = 77
print(bpm)

if bpm > 90:
    bpm = 120

elif bpm < 70:
    bpm = 30

piano1 = session.new_part("Piano")
piano2 = session.new_part("Piano")


pitches = get_pressure()
# pitches = sorted(pitches)
pitches.append(bpm)
for pitch in pitches:
    if pitch < 10:
        pitch = pitch * 8
        if pitch < 2:
            pitch = 15
    if pitch > 90:
        pitch = pitch * 0.96

print(pitches)


def piano_part(which_piano):
    while True:
        for pitch in pitches:
            which_piano.play_note(pitch, 1.0, 0.5)

clock1 = session.fork(piano_part, args=(piano1,), initial_tempo=bpm)
clock2 = session.fork(piano_part, args=(piano2,), initial_tempo=bpm-10)

session.start_transcribing(clock=clock1)
session.wait(10)

performance = session.stop_transcribing()