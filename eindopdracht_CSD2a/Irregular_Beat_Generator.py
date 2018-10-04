"""
1. BPM
2. Samples (laag, hoog, mid)
3. Vragen naar welke maatsoort
4. Random gegenereerde beat
5. Vragen naar opslaan als MIDI-file
6. terug naar 4
7. Stopfuntie --> opgeslagen "Wil je stoppen?"
"""
import time
import simpleaudio as sa
import random

wave_obj_snare = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Hihat.wav")

#-----------function-----------#
def bpm(BPM):
    BPM * (noteLength / 60)

def playSnare():
    play_obj = wave_obj_snare.play()

def playKick():
    play_obj = wave_obj_kick.play()

def playHihat():
    play_obj = wave_obj_hihat.play()
#-----------input-----------#
BPM = int(input("BPM: "))

   
"""
Input gebruiker:
1. BPM

2. Maatsoort (7/8 of 5/4)


3. Opslaan als MIDI-file? (Ja / Nee)
    When Ja:
        Quit? (Ja / Nee)
        When Ja:
            exit
        Else:
            repeat from 3.
    Else:
        repeat from 3
"""
