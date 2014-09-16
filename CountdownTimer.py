import time
import subprocess

theVar = None

def loop_a():
    theVar = ""
    while True:
        subprocess.Popen(["espeak", "Type the task you want to work on now."])
        theVar = raw_input()
        subprocess.Popen(["espeak", "Type the number of minutes you want to work."])
        numMinutes = int(raw_input())
        for i in range(0, numMinutes):
            subprocess.Popen(["espeak", theVar + ". " + str(numMinutes - i) + " minutes remaining."])
            time.sleep(60)
            print(theVar)
        
loop_a()