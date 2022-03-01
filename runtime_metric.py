# Ethan Norton
# This file displays various run time metrics that can be imported into a given jupyter notebook.
# Runtiume metric is used to process resource usage that is collected via name-value pair collcetion. 
    # Essentially, this measures a runtime's performance. 
    # In the context of this problem .... 

import globals
import __init__
import timeit

def test(n):
    return sum(range(n))

n = 10000
loop = 1000

result = timeit.timeit('test(n)', globals=globals(), number=loop)
print(result / loop)
# 0.0002666301020071842


%time: Time the execution of a single statement
%timeit: Time repeated execution of a single statement for more accuracy
%prun: Run code with the profiler
%lprun: Run code with the line-by-line profiler
%memit: Measure the memory use of a single statement
%mprun: Run code with the line-by-line memory profiler
