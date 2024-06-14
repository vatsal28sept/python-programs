# Recursive Function 
# Create A Recursive Function To Calculate Factorial Of A Number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with the desired number
result = factorial(5)
print("The factorial of 5 is:", result)
