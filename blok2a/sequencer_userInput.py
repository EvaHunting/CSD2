import simpleaudio as sa
import time
import random

"""
An example project in which a rhythmical sequence (one measure, 1 sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4
Instead of using steps to iterate through a sequence, we are checking the time.
We will trigger events based on a timestamp.
------ HANDS-ON TIPS ------
- Run the code, read the code and answer the following question:
  - This script transforms a list of 'sixteenth notes timestamps' into a list of
    regular timestamps.
    In the playback loop, the time difference (currentTime minus startTime)
    is compared to the upcomming timestamp.
    Why is this a more accurate method then the methods used in the examples
    "04_randomNoteDuration.py" and "05_oneSampleSequenceSteps.py"?
    Notate your answer below this line (Dutch is allowed)!
    Omdat er geen vertraging meer zit door de time.sleep
- Alter the code:
  Currently one sample is played. Add another sample to the script.
  When a sample needs to be played, choose one of the two samples
  randomly.
  (See the hint about the random package in script "02_timedPlayback".)
- Alter the code:
  Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The timestamps list is emptied using the pop() function.
  (multiple possible solutions)
"""

# load 1 audioFile and store it into a list
# note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Snare.wav"), sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Hihat.wav")]
# set bpm
bpm = int(input("BPM = "))
# calculate the duration of a quarter note
quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

# create a list to hold the timestamps
timestamps = []
timestamps16th = []

# create a list with ‘note timestamps' in 16th at which we should play the sample
noteDurations_nolist = input("List of durations notes (16th): ")
noteDurations = [float(x) for x in noteDurations_nolist.split(", ")]

def durationToTimestamps16th(noteDurations):
  currentTime = 0
  for note in noteDurations:
    currentTime += note * sixteenthNoteDuration 
    timestamps16th.append(currentTime)

durationToTimestamps16th(noteDurations)
    
print(timestamps16th)

# transform the sixteenthTimestamps to a timestamps list with time values
for timestamp in timestamps16th:
  timestamps.append(timestamp * sixteenthNoteDuration)

# retrieve first timestamp
# NOTE: pop(0) returns and removes the element at index 0
timestamp = timestamps.pop(0)
# retrieve the startime: current time
startTime = time.time()
keepPlaying = True
# play the sequence
while keepPlaying:
  # retrieve current time
  currentTime = time.time()
  # check if the timestamp's time is passed
  if(currentTime - startTime >= timestamp):
    # play sample
    samples[random.randint(0, 1)].play()

    # if there are timestamps left in the timestamps list
    if timestamps:
      # retrieve the next timestamp
      timestamp = timestamps.pop(0)
    else:
      # list is empty, stop loop
      keepPlaying = False
  else:
    # wait for a very short moment
    time.sleep(0.001)

