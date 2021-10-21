from playsound import playsound
import random
import time
contador = 0
stopValue = random.randint(0,6)
print(stopValue)
while contador < stopValue:
    contador +=1
    time.sleep(.2)
    print(contador)
    if contador == stopValue:
        playsound('alarm.mp3')