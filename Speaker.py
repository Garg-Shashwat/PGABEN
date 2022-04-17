import argparse
import pyttsx3
import time

def secondsToMinutes(time_s):
    return round(time_s/60,2)

parser = argparse.ArgumentParser()
parser.add_argument("--time","-t",dest="time")
args = parser.parse_args()
total_time = int(args.time)
print(total_time)

#The Speaking Part
engine = pyttsx3.init()
#engine.setProperty('rate')

#Reminding Part : Intervals are of form 50%, 75% and 60 seconds before completion
rm_time = int(total_time)
reminding = []
reminding.append(int(total_time * 0.5)) # 50%
reminding.append(int(total_time * 0.25)) # 25%
reminding.append(int((total_time * 0.25) - 60)) # 25% - 60 seconds
#reminding.append((total_time * 0.98) - (total_time * 0.9))
print(reminding)
for wait_time in reminding:
    if wait_time >= 0:
        time.sleep(wait_time)
        rm_time = rm_time - wait_time
        engine.say(f"{secondsToMinutes(rm_time)} minutes remaining.")
        print(f"Remaining Time = {rm_time} seconds")
        engine.runAndWait()
