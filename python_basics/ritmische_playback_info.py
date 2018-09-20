import simpleaudio as sa
import time


# list with values
# number of items in list
# forloop

values = [0.5, 0.25, 0.5, 2, 1]
#retrieve length of list
numValues = len(values)

#----------------------------------------#

# print values to controll with time delay
print(" ")
for value in values:
    print(value)
    
# print i numValues number of times
#   optie 1  #
print(" ")
for i in range(numValues):
    print(i)

#   optie 2  #
print(" ")
startValue = 10
for i in range(startValue, startValue + numValues):
    print(i)

#-----------------------------------------#
#   optie 1     #
print(" ")
print("first forloop")
for index, value in enumerate(values):
    print(index)
    print(value)

#   optie 2    #
print(" ")
print("second forloop")
for index in range(len(values)):
    print(index)
    print(values[index])

#-----------------------------------------#
print(" ")
for value in values:
    print(value)
    for value2 in values:
        print(value2)

#-----------------------------------------#
numValues = len(values)

for value in values:
    print(value)
    time.sleep(value)
