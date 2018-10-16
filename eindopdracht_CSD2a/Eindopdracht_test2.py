import time
import simpleaudio as sa
import random
import mido

#inladen samples
wave_obj_snare = sa.WaveObject.from_wave_file("../python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("../python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")


timeStamp = [0, 1, 2, 3, 4, 5]

BPM = int(input("BPM: "))

bpm = 

quarterNoteDuration = 60 / bpm


def playSnare():
    play_obj = wave_obj_snare.play()

def playKick():
    play_obj = wave_obj_kick.play()

def playHihat():
    play_obj = wave_obj_hihat.play()



def laag1():
    for x in timeStamp:
        random.randint(0, 1)
        if x == 0:
            time.sleep(1 * quarterNoteDuration)
        else:
            return playkick()

laag1()

