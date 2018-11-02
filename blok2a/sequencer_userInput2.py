#----------Imports-----------#
import simpleaudio as sa
import time
import random

#----------Variables-----------#
samples = [sa.WaveObject.from_wave_file("../python_basics/Snare.wav"), sa.WaveObject.from_wave_file("../python_basics/Hihat.wav")]
bpm = int(input("BPM = "))

#duration notes
quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0

#list timestamps in 16th
noteDurations_nolist = input("List of durations 16th notes (bijv. 0.5, 2.0, 1.0): ")
noteDurations = [float(x) for x in noteDurations_nolist.split(", ")]

# create a list to hold the timestamps
timestamps = []
  
#-----------Functions----------#
def durationToTimestamps(noteDurations):
  currentTime = 0
  for note in noteDurations:
    currentTime += note * sixteenthNoteDuration 
    timestamps.append(currentTime)


def playSequencer(timestamps):
    timestamp = timestamps.pop(0)
    startTime = time.time()
    keepPlaying = True
    while keepPlaying:
        currentTime = time.time()
        if (currentTime - startTime >= timestamp):
            samples[random.randint(0, 1)].play()
            if timestamps:
                timestamp = timestamps.pop(0)
            else:
                keepPlaying = False
        else:
            time.sleep(0.001)

durationToTimestamps(noteDurations)
print(timestamps)
playSequencer(timestamps)


