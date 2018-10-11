import time
import simpleaudio as sa
import random
import mido

#inladen samples
wave_obj_snare = sa.WaveObject.from_wave_file("../python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("../python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")

noteLength_choice = [0.5, 1.0, 1.5, 2.0]
noteLengths1 = []

def laag1():
    randomNote1 = random.choice(noteLength_choice)
    noteLengths1.append(randomNote1)
    if len(noteLengths1) == 5:
        print(noteLengths1)
        return 0
    else:
        return laag1()

laag1()
