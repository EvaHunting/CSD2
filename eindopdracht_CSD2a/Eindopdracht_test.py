import time
import simpleaudio as sa
import random
import mido
import midiutil
from midiutil.MidiFile import MIDIFile

BPM = int(input("BPM: "))
noteLengths1_VV = [0.5, 2, 1, 1.5]
noteLengths2_VV = [2, 0.5, 1.5, 1]
noteLengths3_VV = [1, 0.5, 1.5, 2]

def MIDI_VV():
    mf = MIDIFile(3)    #3 tracks
    startTime = 0       #begint bij het begin
    track = 0
    mf.addTrackName(track, startTime, "5/4 Beat")
    mf.addTempo(track, startTime, BPM)
    if len(noteLengths1_VV) == 0:
        print("Kick Done")
        #write to disk
        with open("output.mid", 'wb') as outf:
            mf.writeFile(outf)
    else:
        track = 0                           #eerste track
        channel = 10                        #percussie
        volume = 100    
        pitch = 35                          #kick
        time = 0                            #startpunt noot
        duration = noteLengths1_VV.pop(0)   #1e nootlengte uit de lijst
        mf.addNote(track, channel, pitch, time, duration, volume)
        print(mf)
        return MIDI_VV()
"""
    if len(noteLengths2_VV) == 0:
        print("Snare Done")
        
    else:
        track = 1                           #tweede track
        startTime = 0        
        channel = 10                        #percussie
        volume = 100    
        instrument = 38                     #snare
        time = 0                            #startpunt noot
        duration = noteLengths2_VV.pop(0)   #1e nootlengte uit de lijst
        mf.addNote(track, channel, instrument, time, duration, volume)
        print(" ")
        return MIDI_VV()

    if len(noteLengths3_VV) == 0:
        print("Hihat Done")
        print("Done")

        #write to disk
        with open("output.mid", 'wb') as outf:
            mf.writeFile(outf)
    else:
        track = 2                           #derde track
        startTime = 0
        channel = 10                        #percussie
        volume = 100    
        instrument = 42                     #hihat
        time = 0                            #startpunt noot
        duration = noteLengths3_VV.pop(0)   #1e nootlengte uit de lijst
        mf.addNote(track, channel, instrument, time, duration, volume)
        print(" ")
        return MIDI_VV()
"""
MIDI_VV()

