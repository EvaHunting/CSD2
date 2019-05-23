import music21 as m21
import random

layer1 = [[60, 1, 100], [63, 2, 80], [64, 1, 60], [59, 4, 100], [72, 1, 100]]
layerOne = []
layerTwo = [60]
options = []

for note in layer1:
    layerOne.append(note[0]) #alle midinootwaardes in een array

#def cadensStart():
#    layerOne[0]

def contrapuntInator():
    verschil = (layerOne[1] - layerOne[0])
    def parallel():
        layerTwo.append(layerOne[0] + verschil)
        layerOne.pop(0)
    def tegenbeweging():
        layerTwo.append(layerOne[0] - verschil)
        layerOne.pop(0)
    def zijdelings():
        layerTwo.append(layerOne[0])
        layerOne.pop(0)
    def zijdelings2():
        layerTwo.append(layerOne[0] + random.choice([1, -1]))
        layerOne.pop(0)


    if (verschil == 3 or verschil == 4 or verschil == 8 or verschil == 9): #tertsen en sexten
        print("zijdelings of tegenbeweging of parallel")
        options.extend([0, 1, 2]) # 0 = zijdelings, 1 = tegenbeweging 2 = parallel
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            print("parallel")
            parallel()
        elif (choice == 1):
            print("tegenbeweging")
            tegenbeweging()
        else:
            print("zijdelings")
            zijdelings()
    elif (verschil == 5 or verschil == 7):  #reine kwart en kwint
        print("tegenbeweging of zijdelings")
        options.extend([0, 1])
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            print("tegenbeweging")
            tegenbeweging()
        else:
            print("zijdelings")
            zijdelings()
    elif (verschil == 0):   #reine prime
        print("zijdelings")
        zijdelings2()
    else:                   #overige intervallen
        print("zijdelings")
        zijdelings()
    if (len(layerOne) > 1):
        contrapuntInator()
    else:
        #TODO: cadens met tegenbeweging
        print("recursion Done")


contrapuntInator()
print(layerOne)
print(layerTwo)
print(layer1)
