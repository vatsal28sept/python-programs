# Age Group Categorization
# Classify a Person's Age Group : Child(<13),Teenager(13-19),Adult(20-59),Senior(60+)
age = int(input("Enter Your Age : "))
if age < 13 :
    print("You Are Child")
elif age > 13 and age <= 19 :
    print("You are Teenager")
elif age >=20 and age <= 59 :
    print("You Are Adult")
else :
    print("You Are Senior")
