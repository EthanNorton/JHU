### Ethan Norton
# This file converts the stacks from stacks that are now appended (prefix mode) into postfix mode.
  ## pop removes an item from the stack, and will be utilized to convert prefix to postfix.
  ## push adds one or more elements to the end of an array. 
  ## This attempts to be as efficient as the knowledge available to the programmer (myself).
  ## Not every stack was able to be converted to postfix. 

# Importing different stacks
import globals 
from StackOfIntegers import globals


# Reverse stack1 for efficient popping (from append).
Reverse(stack1)

# Converting stack1 to postfix 

 ## popping the variables out of prefix 
  stack1.pop(-)
  stack1.pop(+)
  stack1.pop(A)
  stack1.pop(B)
  stack1.pop(C)
  
   ## pushing the variables into postfix
  stack1.push(A)
  stack1.push(B)
  stack1.push(+)
  stack1.push(C)
  stack1.push(-)
  
  
# Reverse stack2 for efficient popping (from append).
Reverse(stack2)

  # Converting stack2 to postfix 
  
   ## popping the variables out of prefix 
  stack2.pop(-)
  stack2.pop(A)
  stack2.pop(+)
  stack2.pop(B)
  stack2.pop(C)
  
  ## pushing the variables into postfix
  stack2.push(A)
  stack2.push(B)
  stack2.push(C)
  stack2.push(+)
  stack2.push(-)
  
  
# Reverse stack3 for efficient popping (from append).
Reverse(stack3)

  # Converting stack3 to postfix 
  
  ## popping the variables out of prefix 
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
  
    ## pushing the variables into postfix
  stack3.push($)
  
# Reverse stack4 for efficient popping (from append).
Reverse(stack4)

  # Converting stack4 to postfix 
  
  ## popping the variables out of prefix 
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
  
  ## pushing the variables into postfix
  stack4.push(A)
  stack4.push($)
  stack4.push(*)
  stack4.push(B)            
  stack4.push(-)     
  
# Reverse stack5 for efficient popping (from append).
Reverse(stack5)

  # Converting stack5 to postfix 
  
  ## popping the variables out of prefix 
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
  
  ## pushing the variables into postfix
 stack5.push(A)
 stack5.push(B)
 stack5.push(C)
 stack5.push(+)
 stack5.push(*)
 stack5.push(C)
 stack5.push(B)
 stack5.push(A)
 stack5.push(-)
 stack5.push(+)
 stack5.push(*)

# Reverse stack6 for efficient popping (from append).
Reverse(stack6)

# Converting stack6 to postfix 

## popping the variables out of prefix
 stack6.pop(/)
 stack6.pop(A)
 stack6.pop(+)
 stack6.pop(B)
 stack6.pop(C)
 stack6.pop( )
 stack6.pop(+)
 stack6.pop(C)
 stack6.pop(*)
 stack6.pop(B)
 stack6.pop(A)

### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
    ## I believe that the space in the stack seperates the two parts, will test this with removing a space from the next input set. 
 
## pushing the variables into postfix 
  stack6.push(A)
  stack6.push(B)
  stack6.push(C)
  stack6.push(+)
  stack6.push(/)
  
  
# Reverse stack7 for efficient popping (from append).
Reverse(stack7)

  # Converting stack7 to postfix 
  
## popping the variables out of prefix
  stack7.pop(/)
  stack7.pop(A)
  stack7.pop(+)
  stack7.pop(B)
  stack7.pop(C)
  stack7.pop(+)
  stack7.pop(C)
  stack7.pop(*)
  stack7.pop(B)
  stack7.pop(A)
  
  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
    ### Previous hypothesis was incorrect. Still not able to convert the full stack to postfix.
  
  ## pushing the variables into postfix
  stack7.push(A)
  stack7.push(B)
  stack7.push(C)
  stack7.push(+)
  stack7.push(/)
  
  
 # Reverse stack8 for efficient popping (from append).
Reverse(stack8)
  
  # Convert Stack8 to Postfix
  
  ## popping the variables out of prefix
  stack8.pop(*)
  stack8.pop(-)
  stack8.pop(*)
  stack8.pop(-)
  stack8.pop(A)
  stack8.pop(B)
  stack8.pop(C)
  stack8.pop(+)
  stack8.pop(B)
  stack8.pop(A)
  
  ## pushing the variables into postfix
  stack8.push(A)
  stack8.push(B)
  stack8.push(-)
  stack8.push(C)
  stack8.push(*)
  stack8.push(B)
  stack8.push(A)
  stack8.push(+)
  stack8.push(-)
  stack8.push(*)
  
# Reverse stack9 for efficient popping (from append).
Reverse(stack9)
  
  # Convert Stack9 to postfix
  
  ## popping the variables out of prefix
  stack9.pop(/)
  stack9.pop(+)
  stack9.pop(/)
  stack9.pop(A)
  stack9.pop(-)
  stack9.pop(B)
  stack9.pop(C)
  stack9.pop(-)
  stack9.pop(B)
  stack9.pop(A)
  
   ## pushing the variables into postfix
  stack9.push(A)
  stack9.push(B)
  stack9.push(C)
  stack9.push(-)
  stack9.push(/)
  stack9.push(B)
  stack9.push(A)
  stack9.push(-)
  stack9.push(+)
  stack9.push(/)
  
# Reverse stack10 for efficient popping (from append).
Reverse(stack10)
  
  # Convert Stack10 to postfix
  
  ## popping the variables out of prefix
  stack10.pop(*)
  stack10.pop($)
  stack10.pop(A)
  stack10.pop(+)
  stack10.pop(B)
  stack10.pop(C)
  stack10.pop(+)
  stack10.pop(C)
  stack10.pop(-)
  stack10.pop(B)
  stack10.pop(A)
  
  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
  
     ## pushing the variables into postfix
  stack10.push($)
  stack10.push(A)
  stack10.push(*)
  
# Reverse stack11 for efficient popping (from append).
Reverse(stack11)
  
  # Convert Stack11 to postfix
  
  ## popping the variables out of prefix
  stack11.pop(/)
  stack11.pop(/)
  stack11.pop(A)
  stack11.pop(+)
  stack11.pop(B)
  stack11.pop(0)
  stack11.pop(-)
  stack11.pop(C)
  stack11.pop(+)
  stack11.pop(B)
  stack11.pop(A)
  
   ## pushing the variables into postfix
  stack11.push(A)
  stack11.push(B)
  stack11.push(0)
  stack11.push(+)
  stack11.push(/)
  stack11.push(C)
  stack11.push(B)
  stack11.push(A)
  stack11.push(+)
  stack11.push(-)
  stack11.push(/)
  
# Reverse stack12 for efficient popping (from append).
Reverse(stack12)
  
  # Convert Stack12 to postfix

   ## popping the variables out of prefix
  stack12.pop(*)
  stack12.pop($)
  stack12.pop(A)
  stack12.pop(^)
  stack12.pop(B)
  stack12.pop(C)
  stack12.pop(+)
  stack12.pop(C)
  stack12.pop(-)
  stack12.pop(B)
  stack12.pop(A)
  
  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
      
  ## pushing the variables into postfix
  stack12.push($)
  stack12.push(A)
  stack12.push(*)
 
# Reverse stack13 for efficient popping (from append).
Reverse(stack13)

 # Convert Stack13 to postfix
  
 ## popping the variables out of prefix
  stack13.pop(+)
  stack13.pop(A)
  stack13.pop(B)
  stack13.pop(C)
  
  ### It is not possible to push this entire prefix into postfix. 
    ### Therefore, the remainder of the code will only convert the postfix equivalent. 
      ### Consider this 1. as a failed case & 2. Dealing with wild input. 
        ## I had no idea of the outcome, but thought how interesting it was that such a small tweak could change the outcome of stack1.
        
   ## pushing the variables into postfix
  stack13.push(A)
  stack13.push(B)
  stack13.push(+)
  
