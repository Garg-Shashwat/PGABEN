#!/usr/bin/python3
import subprocess
import os

def GetFileName(file_path):
    return (os.path.basename(file_path)).title()

def Starting_Text():
    print("This has been created by Sanchay Joshi under the GNU Affero General Public License v3.0")
    print("NOTE: THIS APPLICATION ONLY RUNS .EXE FILES")
    print("------------------------------")

def open_the_process(path):
    #TODO: Find a way to add \ path in input
    time = float(input('Enter time in minutes\n'))
    print(path)
    time = time * 60
    print("Starting for ",time,"seconds")
    subprocess.run(path,timeout=int(time))

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