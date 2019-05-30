import music21 as m21
import random

layer1 = [[60, 1, 100], [62, 2, 80], [64, 1, 60], [62, 4, 100]]
layerOne = []
layerOneCopy = []
layer01 = []
layer2 = []
durations = []
durations2 = []

options = []

for note in layer1:
    layerOne.append(note[0]) #alle midinootwaardes in een array
    layerOneCopy.append(note[0])
for duration in layer1:
    durations.append(duration[1]) #alle durations in een array

layerTwo = [(layerOne[0])] #eerste noot van layertwo is eerste noot van layerOne

def getLastNote():
    global lastNote
    lastNote = layerOne[0]
    return lastNote
def parallel():
    global verschil
    layerTwo.append(layerOne[0] + verschil)
    getLastNote()
    layerOne.pop(0)
    return lastNote
def tegenbeweging():
    global verschil
    layerTwo.append(layerOne[0] - verschil)
    getLastNote()
    layerOne.pop(0)
    return lastNote
def zijdelings():
    layerTwo.append(layerOne[0])
    getLastNote()
    layerOne.pop(0)
    return lastNote
def zijdelings2():
    layerTwo.append(layerOne[0] + random.choice([1, -1, 2, -2]))
    getLastNote()
    layerOne.pop(0)
    return lastNote
def einde():
    afstand = abs(layerTwo[-1] - layerOne[-1])
    if (afstand != 3 or afstand != 4):
        if (afstand > 4):
            layerOne.append(layerOne[0])
            layerOneCopy.append(layerOne[0])
            layer1.append(layerOne[0])
            layerTwo.append(layerTwo[-1] + random.choice([1, 2]))
            einde()
        elif (afstand < 3):
            layerOne.append(layerOne[0])
            layerOneCopy.append(layerOne[0])
            layer1.append(layerOne[0])
            layerTwo.append(layerTwo[-1] - random.choice([1, 2]))
            einde()
        elif (afstand == 3):
            layerTwo.append(layerTwo[-1] + 1)
            layerOne.append(layerOne[0] - 2)
            layerOneCopy.append(layerOne[0] - 2)
            layer1.append(layerOne[0] - 2)
            return layerOne, layerTwo
        else:
            layerTwo.append(layerTwo[-1] + 2)
            layerOne.append(layerOne[0] - 2)
            layerOneCopy.append(layerOne[0] - 2)
            layer1.append(layerOne[0] - 2)
            return layerOne, layerTwo

def contrapuntInator():
    global lastNote
    global verschil
    verschil = (layerOne[1] - layerOne[0])
    interval = (layerTwo[0] - lastNote)
    if (interval == 3 or interval == 4 or interval == 8 or interval == 9): #tertsen en sexten
        print("zijdelings of tegenbeweging of parallel")
        options.extend([0, 1, 2]) # 0 = zijdelings, 1 = tegenbeweging 2 = parallel
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            print("parallel")
            lastNote = parallel()
        elif (choice == 1):
            print("tegenbeweging")
            lastNote = tegenbeweging()
        else:
            print("zijdelings")
            lastNote = zijdelings()
    elif (interval == 5 or interval == 7):  #reine kwart en kwint
        print("tegenbeweging of zijdelings")
        options.extend([0, 1])
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            print("tegenbeweging")
            lastNote = tegenbeweging()
        else:
            print("zijdelings")
            lastNote = zijdelings()
    elif (interval == 0 or interval == 12): #prime en octaaf
        print("tegenbeweging")
        lastNote = tegenbeweging()
    elif (verschil == 0):   #reine prime
        print("zijdelings")
        lastNote = zijdelings2()
    else:                   #overige intervallen
        print("zijdelings")
        lastNote = zijdelings()
    if (len(layerOne) > 1):
        contrapuntInator()
    else:
        #TODO: cadens met tegenbeweging
        print("recursion Done")
        einde()

def layer01Maker():
    for duration in layer2:
        durations.append(duration[1])
    for note in layerOneCopy:
        try:
            duration = int(durations[0])
            durations.pop(0)
        except:
            duration = 4
        layer01.append([note, duration, 120])

    return layer01


def layer2Maker():
    options.extend([1, 2, 4, 8])
    for note in layerTwo:
        durations2.append(random.choice(options))
        try:
            duration = int(durations[0])
            durations.pop(0)
        except:
            duration = durations2[-1]
        layer2.append([note, duration, 120])
    durations2.clear()
    options.clear()
    return layer2



verschil = 0;
lastNote = getLastNote()
contrapuntInator()
layer2Maker()
layer01Maker()
print(layer2)
print(layer01)
