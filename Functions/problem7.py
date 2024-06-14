# Functions With *args 
# Writr A Function That Takes Variable Number Of Argument And Return Their Sum 

def sum_all(*args):
    return sum(args)
print(sum_all(1,1,3))
print(sum_all(1,1,4,8,93))
print(sum_all(1,1,4,8,9,85,86))