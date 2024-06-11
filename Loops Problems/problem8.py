# Prime Number Checker 
# Check If A Number Is Prime
number = int(input("Enter The Number : "))
is_prime = True
if number>1:
    for i in range(2,number):
        if(number%i == 0):
            is_prime=False
            break
print(number,"Is Prime Number")