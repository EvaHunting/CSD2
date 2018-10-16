import time
import simpleaudio as sa
import random
import mido

#inladen samples
wave_obj_snare = sa.WaveObject.from_wave_file("../python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("../python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")

noteLength_choice = [0.0, 0.5, 1.0, 1.5, 2.0]
noteLengths1 = []
noteLengths2 = []
noteLengths3 = []

def laag1():
    randomNote1 = random.choice(noteLength_choice)
    noteLengths1.append(randomNote1)
    if len(noteLengths1) == 5:
        print(noteLengths1)
        return 0
    else:
        return laag1()

def laag2():
    randomNote2 = random.choice(noteLength_choice)
    noteLengths2.append(randomNote2)
    if len(noteLengths2) == 5:
        print(noteLengths2)
        return 0
    else:
        return laag2()    

def laag3():
    randomNote3 = random.choice(noteLength_choice)
    noteLengths3.append(randomNote3)
    if len(noteLengths3) == 5:
        print(noteLengths3)
        return 0
    else:
        return laag3()

laag1()
laag2()
laag3()
