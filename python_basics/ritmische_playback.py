import simpleaudio as sa
import time

# list with values
# number of items in list
# forloop

wave_obj = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Snare.wav")
times = int(input("insert the number of times you would like to hear this sound: "))
BPM = int(input("BPM: "))
values = [0.5, 0.25, 0.5, 0.75, 1]
numValues = len(values)

def playSnare():
    for value in values:
        print(value)
        time.sleep(BPM * (value / 60))

        play_obj = wave_obj.play()

def numPlaybackTimes(times):
    if numPlaybackTimes == 0:
        print("Done")
        return 0
    else:
        playSnare()
        print(times)
        return playSnare()
        return (times - 1)

numPlaybackTimes(times)
