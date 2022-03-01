### Ethan Norton
# Input and Read the Characters line by line.
# Main = LAUNCH the program or the entry point
# This file connects all code, and is best for connecting the other source code found throughout the document.
# This file combines all of the source code, and produces the output that is found in the output file.

# Reading The file, so it is inputable into various stacks
# Copy and paste code sniper from blackboard.
f = open('in.txt', 'r') #This reads the file. #change file name back
f = Path('in.txt')
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

# inputting variables (stacks 1-13)

import globals
from StackOfIntegers import globals 
from prefixtopostfix import globals
from runtime_metric import ...


