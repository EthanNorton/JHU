# Stack using Python List
  # append pushes an item in the stack (will do row by row from the input file).

# Reading The file, so it is inputable into various stacks
f = open('in.txt', 'r') #This reads the file.
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



# Inputing the stack1
stack1 = list()
  stack1.append(-)
  stack1.append(+)
  stack1.append(A)
  stack1.append(B)
  stack1.append(C)
  print(stack1)
  
 
# Inputing the stack2
stack2 = list()
  stack2.append(-)
  stack2.append(A)
  stack2.append(+)
  stack2.append(B)
  stack2.append(C)
  print(stack2)
 
# Inputing the stack3
stack3 = list()
  stack3.append($)
  stack3.append(+)
  stack3.append(-)
  stack3.append(A)
  stack3.append(B)
  stack3.append(C)
  stack3.append(+)
  stack3.append(D)
  stack3.append(-)
  stack3.append(E)
  stack3.append(F)
  print(stack3)
 
# Inputing the stack4
stack4 = list()
  stack4.append(-)
  stack4.append(*)
  stack4.append(A)
  stack4.append($)
  stack4.append(B)
  stack4.append(+)
  stack4.append(C)
  stack4.append(-)
  stack4.append(D)
  stack4.append(E)
  stack4.append(*)
  stack4.append(E)
  stack4.append(F)
  print(stack4)
  
 # Inputing the stack5
 stack5 = list()
  stack5.append(*)
  stack5.append(*)
  stack5.append(A)
  stack5.append(+)
  stack5.append(B)
  stack5.append(C)
  stack5.append(+)
  stack5.append(C)
  stack5.append(-)
  stack5.append(B)
  stack5.append(A)
  print(stack5)
 
# Inputing the stack6
 stack6 = list()
  stack6.append(/)
  stack6.append(A)
  stack6.append(+)
  stack6.append(B)
  stack6.append(C)
  stack6.append( )
  stack6.append(+)
  stack6.append(C)
  stack6.append(*)
  stack6.append(B)
  stack6.append(A)
  print(stack6)
 
# Inputing the stack7
 stack7 = list()
  stack7.append(/)
  stack7.append(A)
  stack7.append(+)
  stack7.append(B)
  stack7.append(C)
  stack7.append( )
  stack7.append(+)
  stack7.append(C)
  stack7.append(*)
  stack7.append(B)
  stack7.append(!)
  print(stack7)
 
# Inputing the stack8
 stack8 = list()
  stack8.append(*)
  stack8.append(-)
  stack8.append(*)
  stack8.append(-)
  stack8.append(A)
  stack8.append(B)
  stack8.append(C)
  stack8.append(+)
  stack8.append(B)
  stack8.append(A)
  print(stack8)
  
# Inputing the stack9
 stack9 = list()
  stack9.append(/)
  stack9.append(+)
  stack9.append(/)
  stack9.append(A)
  stack9.append(-)
  stack9.append(B)
  stack9.append(C)
  stack9.append(-)
  stack9.append(B)
  stack9.append(A)
  print(stack9)
 
# Inputing the stack10
 stack10 = list()
  stack10.append(*)
  stack10.append($)
  stack10.append(A)
  stack10.append(+)
  stack10.append(B)
  stack10.append(C)
  stack10.append(+)
  stack10.append(C)
  stack10.append(-)
  stack10.append(B)
  stack10.append(A)
  print(stack10)
  
# Inputing the stack11
 stack11 = list()
  stack11.append(/)
  stack11.append(/)
  stack11.append(A)
  stack11.append(+)
  stack11.append(B)
  stack11.append(0)
  stack11.append(-)
  stack11.append(C)
  stack11.append(+)
  stack11.append(B)
  stack11.append(A)
  print(stack11)
 
# Inputing the stack12
stack12 = list()
  stack12.append(*)
  stack12.append($)
  stack12.append(A)
  stack12.append(^)
  stack12.append(B)
  stack12.append(C)
  stack12.append(+)
  stack12.append(C)
  stack12.append(-)
  stack12.append(B)
  stack12.append(A)
  print(stack12)

# Inputing the stack13
stack13 = list()
  stack13.append(+)
  stack13.append(A)
  stack13.append(B)
  stack13.append(C)
  print(stack13)

  
# Stack with a Wrapper Class

class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
