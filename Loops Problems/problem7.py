# Validate Input 
# Keep Asking The User For Input Until They Enter Between 1 To 10 

while True:
    number = int(input("Enter The Value Between 1 To 10 :"))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number ,Try Again")