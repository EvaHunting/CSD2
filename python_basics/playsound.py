import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("/Users/evahunting/CSD2/python_basics/Quack.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
