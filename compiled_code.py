# Ethan Norton
# This file connects all code, and is best for connecting the other source code found throughout the document.
# This file combines all of the source code, and produces the output that is found in the output file.
  # This attempts to efficiently convert all prefix to postfix, through the stacks data structure. 

import globals 
import test 
 
if __name__ == "__main__": 
    globals.initialize() 
    print( globals.num ) # print the initial value 
    test.increment() 
    print( globals.num ) # print the value after being modified within test.py 
  
# This will store the stack and allow data enhancement for data clarity. 
stack = []

 operators = {'+', '-', '*', '/', '$'} #This includes all operators that will be displayed in this lab.
# An additional error check in other cases beyond the above specified input would be to include other operators that are not shown in this input.
  #For example, other inputs could possibly utilize the operators @,^,!,=...
    #In this event, it would be important to edit the list of operators to fix this.
 

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
