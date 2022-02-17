import argparse
import pyttsx3
import time

parser = argparse.ArgumentParser()
parser.add_argument("--time","-t",dest="time")
args = parser.parse_args()
total_time = float(args.time)
print(total_time)

#The Speaking Part
engine = pyttsx3.init()
#engine.setProperty('rate')

#Reminding Part
rm_time = int(total_time)
reminding = []
reminding.append(int(total_time * 0.5))
reminding.append(int(total_time * 0.4))
reminding.append(int((total_time * 0.1) - 60))
#reminding.append((total_time * 0.98) - (total_time * 0.9))
print(reminding)
for wait_time in reminding:
    if wait_time > 0:
        time.sleep(wait_time)
        rm_time = rm_time - wait_time
        engine.say(f"{rm_time} seconds remaining")
        engine.runAndWait()
