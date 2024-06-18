# Number Is Odd Or Even 

num = int(input("Enter The Number : "))
def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_or_even(num))