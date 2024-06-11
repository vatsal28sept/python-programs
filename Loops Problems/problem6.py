# Factorial Calculator 
# Compute The Factorial Of A Number Using A While Loop

num = int(input("Enter The Value Of n : " ))
factorial = 1
while num >1 :
    factorial = factorial*num
    num = num - 1
print("Factorial : ",factorial )