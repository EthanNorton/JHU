# Ethan Norton
#Input and Read the Characters line by line.
#Main = LAUNCH the program
import argparse
from pathlib import Path #this is a standard library
!pip install -Uqq ipdb
import ipdb
from proj1 import process_files 

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
arg_parser.add_argument("-s", "--some-int", type=int, default=0,
                        required=False)
args = arg_parser.parse_args()
print(args.some_int)

def read_one_write_another(input_file, output):
  in_path = Path(input_file)
  out_path = Path(output)
  with in_path.open('r') as input_file, out_path.open('w') as output_file:
    process_files(input_file, output_file)
   print("all_done')
  
 read_one_write_another(args.in_file, args.out_file)

# This will store the stack and allow data enhancement for data clarity. 
stack = []

def prefixToInfix(expr):
  operators = {'+', '-', '*', '/', '$'} #This includes all operators that will be displayed in this lab.
# An additional error check in other cases beyond the above specified input would be to include other operators that are not shown in this input.
  #For example, other inputs could possibly utilize the operators @,^,!,=...
    #In this event, it would be important to edit the list of operators to fix this.
  expr = expr.split(" ")
  stack = deque()
  for i in range(len(expr)-1, -1, -1):
    symbol = expr[i]
    if symbol in operators:
     subexpr = f"({stack.pop()} {symbol} {stack.pop()})"
     stack.append(subexpr)
    else:
      stack.append(symbol)
  return stack.pop()

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
