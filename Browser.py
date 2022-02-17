#This code is for testing purposes.
#Copied from https://stackoverflow.com/questions/19944712/browse-for-file-path-in-python AND
#https://www.tutorialspoint.com/askopenfile-function-in-python-tkinter
from tkinter import *
from tkinter import filedialog
base = Tk()

base.geometry("150x150")
# Function for opening the file
def file_opener():
   input = filedialog.askopenfilename(parent=base, initialdir= "/", title='Please select an exe')
   print(input)
   with open("locations.txt",'a') as file:
       file.write(input + "\n")
# Button label
x = Button(base, text ='Select a .exe file', command = lambda:file_opener())
x.pack()
mainloop()