# Stack using Python List
  # This utilizes a LIFO data structure (last in first out).
  # append pushes an item in the stack (will do row by row from the iinput file).
  # pop removes an item from the stack, and will be utilized to convert prefix to postfix. 

stack1 = list()
  stack1.append()
  stack1.append()
  stack1.append()
  stack1.append()
  stack1.append()
  print(stack1)

  
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
