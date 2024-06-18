# Get Time Of A Python Programm's Execution.

import time
def MyFunc():
    start_time = time.time()
    s = 0 
    for i in range(1 , n+1) :
        s = s + i
    end_time = time.time()
    return s , end_time-start_time
n = 5
print(MyFunc())