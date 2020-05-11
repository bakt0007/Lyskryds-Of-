#Lyskryds(Obligatorisk)
#På en Raspberry Pi laves et program der simulere et lyskryds.
#Der skal være 3 led Nord-syd og 3 Øst-vest. Statemachine udarbejdes og koden i Github.


from random import random
import time

def grønlys1():
    print('\x1b[7;32;40m' + "Grøn1! Kør" + '\x1b[0m')
    print('\x1b[6;30;41m' + "RØD2! stop" + '\x1b[0m')
    print()
    time.sleep(3)
    return gullys1


def gullys1():
    print('\x1b[6;30;43m' + "Gul1! stop" + '\x1b[0m')
    print('\x1b[6;30;41m' + "RØD2! stop" + '\x1b[0m')
    print()
    time.sleep(1.5)
    return rødlys1


def rødlys1():
    print('\x1b[6;30;41m' + "RØD1! stop" + '\x1b[0m')
    print('\x1b[6;30;41m' + "RØD2! stop" + '\x1b[0m')
    print('\x1b[6;30;43m' + "Gul2! stop" + '\x1b[0m')
    print()
    time.sleep(3)
    return rød_gullys1()


def rød_gullys1():
    print('\x1b[6;30;41m' + "RØD1! stop" + '\x1b[0m')
    print('\x1b[7;32;40m' + "Grøn2! Kør" + '\x1b[0m')
    print()
    time.sleep(1.5)
    return grønlys1


state=grønlys1()
while state: state=state()
print("Traffik lyskrys!!!")
