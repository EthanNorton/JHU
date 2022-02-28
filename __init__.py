# Ethan Norton
# This file converts the stacks from stacks that are now appended (prefix mode) into postfix mode.
  ## pop removes an item from the stack, and will be utilized to convert prefix to postfix.
  ## push adds one or more elements to the end of an array. 

# Importing different stacks
from StackOfIntegers import stack1
from StackOfIntegers import stack2
from StackOfIntegers import stack3
from StackOfIntegers import stack4
from StackOfIntegers import stack5
from StackOfIntegers import stack6
from StackOfIntegers import stack7
from StackOfIntegers import stack8
from StackOfIntegers import stack9
from StackOfIntegers import stack10
from StackOfIntegers import stack11
from StackOfIntegers import stack12
from StackOfIntegers import stack13

# Converting stack1 to postfix 
  stack1.pop(-)
  stack1.pop(+)
  stack1.pop(A)
  stack1.pop(B)
  stack1.pop(C)
  
  stack1.push(-)
  stack1.push(C)
  stack1.push(+)
  stack1.push(B)
  stack1.push(A)
  stack1 # do i need to explain the logic? for all the variables?
  
  
  # Converting stack2 to postfix 
  stack2.pop(-)
  stack2.pop(A)
  stack2.pop(+)
  stack2.pop(B)
  stack2.pop(C)
  
  stack2.push(-)
  stack2.push(+)
  stack2.push(A)
  stack2.push(B)
  stack2.push(C)
  
  
  # Converting stack3 to postfix 
  stack3.pop($)
  stack3.pop(+)
  stack3.pop(-)
  stack3.pop(A)
  stack3.pop(B)
  stack3.pop(C)
  stack3.pop(+)
  stack3.pop(D)
  stack3.pop(-)
  stack3.pop(E)
  stack3.pop(F)
  
  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
  
  stack3.push(D)
  stack3.push(E)
  stack3.push(F)
  stack3.push(-)
  stack3.push(+)
  
  # Converting stack4 to postfix 
  stack4.pop(-)
  stack4.pop(*)
  stack4.pop(A)
  stack4.pop($)
  stack4.pop(B)
  stack4.pop(+)
  stack4.pop(C)
  stack4.pop(-)
  stack4.pop(D)
  stack4.pop(E)
  stack4.pop(*)
  stack4.pop(E)
  stack4.pop(F)

  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
  
  stack3.push(E)
  stack3.push(F)
  stack3.push(*)
  
  #Converting stack5 to postfix 
  
  ## popping the variables out of postfix 
 stack5.pop(*)
 stack5.pop(*)
 stack5.pop(A)
 stack5.pop(+)
 stack5.pop(B)
 stack5.pop(C)
 stack5.pop(+)
 stack5.pop(C)
 stack5.pop(-)
 stack5.pop(B)
 stack5.pop(A)
  
  ## pushing the variables into prefix
 stack5.pop(*)
 stack5.pop(*)
 stack5.pop(A)
 stack5.pop(+)
 stack5.pop(B)
 stack5.pop(C)
 stack5.pop(+)
 stack5.pop(C)
 stack5.pop(-)
 stack5.pop(B)
 stack5.pop(A)
