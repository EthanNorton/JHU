### Ethan Norton
# Input and Read the Characters line by line.
# Main = LAUNCH the program or the entry point
# This file connects all code, and is best for connecting the other source code found throughout the document.
# This file combines all of the source code, and produces the output that is found in the output file.

# Reading The file, so it is inputable into various stacks
# Copy and paste code sniper from blackboard.
# Assumes there is a file called 'some_file.txt' in this directory
test_file = Path('some_file.txt')
with test_file.open('r') as opened_file:
    while True:
        char = opened_file.read(1)
        if not char:
            print("End of file")
            break
        elif char == '\n':
            print("----New Line----")
        else:
            print(f"Read this char: {char}")

# inputting variables (stacks 1-13)

import globals
from StackOfIntegers import globals 
from prefixtopostfix import globals
from runtime_metric import ...


