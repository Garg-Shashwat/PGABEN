#!/usr/bin/python3
import subprocess
import os

def GetFileName(file_path):
    return (os.path.basename(file_path)).title().strip('"')

def Starting_Text():
    print("This has been created by Sanchay Joshi under the GNU Affero General Public License v3.0")
    print("NOTE: THIS APPLICATION ONLY RUNS .EXE FILES")
    print("------------------------------")

def open_the_process(path):
    '''
    We move to the directory where the game is installed. Some games 
    need to be executed from the directory where they are installed
    for no issues. (Example: Skyrim)
    '''
    time = float(input('Enter time in minutes\n'))
    print(path)
    time = time * 60
    '''
    If the application is to be run for less than 2 minutes, then there is no need
    for the speaking funcitonality to work. Therefore the below code ensures that
    if application is to be run for less than 2 minutes, the user will be prompted
    that speaking functionality will not work and they can decide whether they still
    want to run the application or not
    '''
    if time < 120:
        print("Time less than 120 seconds (2 minutes). Speaking Function will not work. Proceed?(y/n)")
        if input().lower() == 'n':
            print("EXITING")
            exit()
    else:
        #Calling Speaker.py
        speaker = subprocess.Popen(f"python Speaker.py --time {time}")
        #Starting the game
    print("Starting for ",time,"seconds")
    os.chdir(os.path.split(path)[0])
    try:
        subprocess.run(path,timeout=int(time))
    except Exception as e:
        print(e)
        pass
    print(f"Terminating Speaker Process with PID = {speaker.pid}")
    speaker.kill()
            

def startup():
    Starting_Text()
    counter = 0
    with open('locations.txt') as file:
        for line in file:
            counter += 1
            index = line.find('=')
            loc = r'{}'.format(line[index+1::].strip())
            games_list[counter] = loc
    print("Kindly Enter the index of the application you wish to run")

games_list = {}
#----------------------
startup()
for key in games_list:
    print(key,':',GetFileName(games_list[key]),end = '\n')

index = int(input("\nEnter the index of the application you wish to run\n"))
try:
    print(games_list[index])
except:
    print("Game does not exist")
    exit()
open_the_process(games_list[index])