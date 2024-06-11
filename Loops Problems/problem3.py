# Multiplication Table Printer
# Print The Multiplication Table For A Given Number Up To 10 , But Skip The Fifth Iteration

num = 10
for i in range(1,10):
    if i == 5:
        continue
    mul = num*i
    print(mul)
    

