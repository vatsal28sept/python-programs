# Swap Two Variable
# Method 1: Using Temporary Variable

x = 10
y = 20
print("Before Swap X:", x)
print("Before Swap Y:", y)
z = x + y
x = z - x
y = z - y 
print("After Swap X:", x)
print("After Swap Y:",y)


# Method 2 : Without Temporary Variable 

a = 2
b = 5
print("Before Swap A:", a)
print("Before Swap B:", b)
a ,b = b,a
print("After Awap A : ",a)
print("After Awap B : ",b)
