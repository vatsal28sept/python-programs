# How To Do A Profile Python Script
import cProfile
def sum():
    print(1,3)
cProfile.run('sum()')