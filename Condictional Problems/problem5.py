# Weather Activity Suggection
#Suggest A Activity Based On Weather(eg:Sunny - Go For Walk,Rainy - Read A Book,Snowy- Buil A Snowman)
weather = str(input("Enter A Wether : "))

if weather == "sunny":
    print("Go For Walk")
elif weather == "rainy":
    print("Read A Book")
elif weather == "snowy":
    print("Build A Snowman")
else:
    print("I Can't Suggest You")
    exit()