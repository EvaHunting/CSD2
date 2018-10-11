"""
1. BPM 
2. Vragen naar welke maatsoort
3. Random gegenereerde beat (uit 3 lagen)
4. Samples koppelen aan beat (laag, hoog, mid)
5. Ritme afspelen
6. Vragen naar opslaan als MIDI-file
7. terug naar 4
8. Stopfuntie --> opgeslagen "Wil je stoppen?"
"""
import time
import simpleaudio as sa
import random
import mido

#inladen samples
wave_obj_snare = sa.WaveObject.from_wave_file("../python_basics/Snare.wav")
wave_obj_kick = sa.WaveObject.from_wave_file("../python_basics/Kick.wav")
wave_obj_hihat = sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")

#noten koppelen aan BPM
quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0

#-----------function-----------#
def bpm(BPM):
    BPM * (noteLength / 60)

def playSnare():
    play_obj = wave_obj_snare.play()

def playKick():
    play_obj = wave_obj_kick.play()

def playHihat():
    play_obj = wave_obj_hihat.play()

def playBeat(maatsoort):
    if maatsoort == 5/4
        
    else
#-----------other-----------#


    
#-----------input-----------#
BPM = int(input("BPM: "))
maatsoort = input("Time signature: 5/4 or 7/8: ")


   
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
