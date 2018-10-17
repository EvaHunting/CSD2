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


"""
#noten koppelen aan BPM
quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0
"""
#-----------functions-----------#
"""
def bpm(BPM):
    BPM * (noteLength / 60)
"""

def playSnare():
    play_obj = wave_obj_snare.play()

def playKick():
    play_obj = wave_obj_kick.play()

def playHihat():
    play_obj = wave_obj_hihat.play()

#---------------------5/4---------------------#
#mogelijke lengtes
noteLength_choice = [0.5, 1.0, 1.5, 2.0]
noteLengths1_VV = []
noteLengths2_VV = []
noteLengths3_VV = []

#ritmes voor laag 1 waarbij de lengte 5 tellen is
def laag1_VV():
    randomNote1 = random.choice(noteLength_choice)
    noteLengths1_VV.append(randomNote1)
    if sum(noteLengths1_VV) == 5:
        print(noteLengths1_VV)
        return 0
    else:
        if sum(noteLengths1_VV) >= 5:
           noteLengths1_VV.clear()
           return laag1_VV()
        else:
            return laag1_VV()

#ritmes voor laag 2 waarbij de lengte 5 tellen is
def laag2_VV():
    randomNote2 = random.choice(noteLength_choice)
    noteLengths2_VV.append(randomNote2)
    if sum(noteLengths2_VV) == 5:
        print(noteLengths2_VV)
        return 0
    else:
        if sum(noteLengths2_VV) >= 5:
           noteLengths2_VV.clear()
           return laag2_VV()
        else:
            return laag2_VV()

#ritmes voor laag 3 waarbij de lengte 5 tellen is
def laag3_VV():
    randomNote3 = random.choice(noteLength_choice)
    noteLengths3_VV.append(randomNote3)
    if sum(noteLengths3_VV) == 5:
        print(noteLengths3_VV)
        return 0
    else:
        if sum(noteLengths3_VV) >= 5:
           noteLengths3_VV.clear()
           return laag3_VV()
        else:
            return laag3_VV()    
#----------------------------------------------#
#---------------------7/8---------------------#
noteLengths1_ZA = []
noteLengths2_ZA = []
noteLengths3_ZA = []

#ritmes voor laag 1 waarbij de lengte 7 tellen is
def laag1_ZA():
    randomNote1 = random.choice(noteLength_choice)
    noteLengths1_ZA.append(randomNote1)
    if sum(noteLengths1_ZA) == 7:
        print(noteLengths1_ZA)
        return 0
    else:
        if sum(noteLengths1_ZA) >= 7:
           noteLengths1_ZA.clear()
           return laag1_ZA()
        else:
            return laag1_ZA()

#ritmes voor laag 2 waarbij de lengte 7 tellen is
def laag2_ZA():
    randomNote2 = random.choice(noteLength_choice)
    noteLengths2_ZA.append(randomNote2)
    if sum(noteLengths2_ZA) == 7:
        print(noteLengths2_ZA)
        return 0
    else:
        if sum(noteLengths2_ZA) >= 7:
           noteLengths2_ZA.clear()
           return laag2_ZA()
        else:
            return laag2_ZA()

#ritmes voor laag 3 waarbij de lengte 7 tellen is
def laag3_ZA():
    randomNote3 = random.choice(noteLength_choice)
    noteLengths3_ZA.append(randomNote3)
    if sum(noteLengths3_ZA) == 7:
        print(noteLengths3_ZA)
        return 0
    else:
        if sum(noteLengths3_ZA) >= 7:
           noteLengths3_ZA.clear()
           return laag3_ZA()
        else:
            return laag3_ZA()
        
#----------------------------------------------#

def playBeat():
    if maatsoort == 5/4:
        print('5/4')
        laag1_VV()
        laag2_VV()
        laag3_VV()
    else:
        print('7/8')
        laag1_ZA()
        laag2_ZA()
        laag3_ZA()
#-----------other-----------#


    
#-----------input-----------#
BPM = int(input("BPM: "))
maatsoort = eval(input("Time signature (5/4 or 7/8): "))

playBeat()

   
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
