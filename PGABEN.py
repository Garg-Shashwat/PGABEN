#!/usr/bin/python3
import subprocess

def open_the_process(path):
    #TODO: Find a way to add \ path in input
    time = float(input('Enter time in minutes\n'))
    print(path)
    time = time * 60
    subprocess.run(path,timeout=int(time))

def startup():
    counter = 0
    with open('locations.txt') as file:
        for line in file:
            counter += 1
            index = line.find('=')
            loc = r'{}'.format(line[index+1::].strip())
            games_list[counter] = loc

games_list = {}
startup()
print("NOTE: THIS APPLICATION ONLY RUNS .EXE FILES")
print("which game do you wish to play?")
for key in games_list:
    print(key,':',games_list[key],end = '')

index = int(input("\nEnter the index of the game you wish to play\n"))
try:
    print(games_list[index])
except:
    print("Game does not exist")
open_the_process(games_list[index])