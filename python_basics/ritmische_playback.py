import simpleaudio as sa
import time

#inladen sample
wave_obj = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Snare.wav")
#times
times = int(input("insert the number of times you would like to hear this sound: "))
#Het BPM van het ritme
BPM = int(input("BPM: "))
#lijst met notenwaardes
noteLength = input('length notes: ')
values = [float(x) for x in noteLength.split(" ")]
numValues = len(values)
print(values)

def playSnare():
    for value in values:
        print(value)
        time.sleep(BPM * (value / 60))

        play_obj = wave_obj.play()

def numPlaybackTimes(times):
    if numPlaybackTimes == 0:
        return 0
    else:
        playSnare()
        return playSnare()
        return (times - 1)

numPlaybackTimes(times)

