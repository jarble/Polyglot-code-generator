#!/usr/bin/env python
from time import sleep
from subprocess import call

def say(toSay):
    call(["espeak", toSay])

def waitAndSpeak(timeToWait, thingsToSay):
    sleep(timeToWait)
    say(thingsToSay)

def countDown(timeInMinutes, toSay, interval):
    #if(timeInMinutes % interval != 0):
    #    raise Exception("The time in minutes, which is " +str(timeInMinutes)+ ", must be divisible by the time interval, which is "+ str(interval))
    for current in range(0, timeInMinutes):
        if (timeInMinutes == 1) or timeInMinutes % interval == 0:
            minuteOrMinutes = "minutes"
            if timeInMinutes == 1:
                minuteOrMinutes = "minute"
            theStr = toSay + ". " + str(timeInMinutes)  + " "+minuteOrMinutes+" remaining. "
            call(["espeak", theStr])
        sleep(60)
        timeInMinutes -= 1;

#for current in ["Read about Pythagorean identities.", "Read about double angle identities", "Read about factoring polynomials.", "Read about partial fraction decomposition"]:
#	countDown(4, current, 2)
