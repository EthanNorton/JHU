# Ethan Norton
# This file displays various run time metrics that can be imported into a given jupyter notebook.
# Runtiume metric is used to process resource usage that is collected via name-value pair collcetion. 
    ## Essentially, this measures a runtime's performance. 
    ## In the context of this problem this can be applied to various stacks (1-13).
    ## A lot of these should be able to be applied in future projects.
    
import globals
from StackOfIntegers import globals 
from prefixtopostfix import globals
import timeit

def test(stackn): #insert stack number(n) here
    return sum(range(stackn)) #insert stack number (n) here


n = 10000
loop = 1000

result = timeit.timeit('test(stackn)', globals=globals(), number=loop) #import stackn where n represents the stack number. 
print(result / loop)
# 0.002341232  - this is an example that measures the execution time of a function.

# different codes to capture various runtime metrics in future projects.

%time: Time the execution of a single statement
%timeit: Time repeated execution of a single statement for more accuracy
%prun: Run code with the profiler
%lprun: Run code with the line-by-line profiler
%memit: Measure the memory use of a single statement
%mprun: Run code with the line-by-line memory profiler
