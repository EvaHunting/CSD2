import simpleaudio as sa

times = int(input("insert the number of times you would like to hear this sound: "));

def total(times):

    if total == 0:
        print("Done");
        return 0
    else:
        wave_obj = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Quack.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()    
        print(times);
        return(times - 1);

total(times);
