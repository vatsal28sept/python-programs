# Counting Positive Numbers
# Give A List Of Numbers ,Count How Many Are Positive
# numbers = [1,-2,3,-4,5,6,-7,9,10]

numbers = [1,-2,3,-4,5,6,-7,9,10]
positive_number = 0
for i in numbers :
    if i>0:
        positive_number += 1
print("Finel Count Of Positive Number Is: ",positive_number)