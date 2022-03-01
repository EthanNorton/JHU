# Ethan Norton
# This file connects all code, and is best for connecting the other source code found throughout the document.
# This file combines all of the source code, and produces the output that is found in the output file.
  # This attempts to efficiently convert all prefix to postfix, through the stacks data structure. 

import globals 
import test 
  

globals.init()          # Call only once
__init__.stuff()         # Do stuff with global var
print settings.myList[0] # Check the result

#This is the beginning of source code.
f = open('some_file.txt', 'r') #This reads the file.
f = Path('some_file.txt')
with f.open('r') as opened_file: #Looks at the file
    while True:
        char = opened_file.read(1) #Reads Characters
        if not char:
            print("End of file") 
            break
        elif char == '\n':
            print("----New Line----") #This ends the line of the stack
        else:
            print(f"Read this char: {char}")  #This displays the character in the given stack 
          #  f.replace(" ", "") .. attempting to replace the blank spaces
