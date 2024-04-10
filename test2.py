from pydub import AudioSegment
import numpy as np
import soundfile as sf
from scamp import *
from microserial import Microbit

m=Microbit()

def get_bpm():
    for i in m:
        if i != "":
            return i
    
def get_pressure():
    values = []
    for i in m:
        if i != "":
            values.append(i)
session = Session()

bpm = get_bpm()
bpm = int(bpm)
print(bpm)

if bpm > 90:
    bpm = 120

elif bpm < 70:
    bpm = 30

piano1 = session.new_part("Piano")
piano2 = session.new_part("Guitar")

pitches = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]


def piano_part(which_piano):
    while True:
        for pitch in pitches:
            which_piano.play_note(pitch, 1.0, 0.25)

clock1 = session.fork(piano_part, args=(piano1,), initial_tempo=bpm)
clock2 = session.fork(piano_part, args=(piano2,), initial_tempo=bpm-1)

session.start_transcribing(clock=clock1)
session.wait(10)

performance = session.stop_transcribing()