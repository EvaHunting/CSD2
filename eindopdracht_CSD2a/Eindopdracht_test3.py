import time
import simpleaudio as sa
import random
import mido

#inladen samples
wave_obj_snare = sa.WaveObject.from_wave_file("../python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("../python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")

#mogelijke lengtes in kwartnoten
noteLength_choice = [0.5, 1.0, 1.5, 2.0]
noteLengths1 = []
noteLengths2 = []
noteLengths3 = []

#ritmes voor laag 1 waarbij de lengte 5 tellen is
def laag1():
    randomNote1 = random.choice(noteLength_choice)
    noteLengths1.append(randomNote1)
    if sum(noteLengths1) == 5:
        print(noteLengths1)
        return 0
    else:
        if sum(noteLengths1) >= 5:
           noteLengths1.clear()
           return laag1()
        else:
            return laag1()

#ritmes voor laag 2 waarbij de lengte 5 tellen is
def laag2():
    randomNote2 = random.choice(noteLength_choice)
    noteLengths2.append(randomNote2)
    if sum(noteLengths2) == 5:
        print(noteLengths2)
        return 0
    else:
        if sum(noteLengths2) >= 5:
           noteLengths2.clear()
           return laag2()
        else:
            return laag2()

#ritmes voor laag 3 waarbij de lengte 5 tellen is
def laag3():
    randomNote3 = random.choice(noteLength_choice)
    noteLengths3.append(randomNote3)
    if sum(noteLengths3) == 5:
        print(noteLengths3)
        return 0
    else:
        if sum(noteLengths3) >= 5:
           noteLengths3.clear()
           return laag3()
        else:
            return laag3()

laag1()
laag2()
laag3()
