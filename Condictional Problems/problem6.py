# Transportation Mode Selection
#Choose a Transportation Mode On The Distance (eg: <3km: walk,3-15km:bike,>15:car)

distance = int(input("Enter Your Distance : "))

if distance < 3 :
    print("Walk")
elif distance >= 3 and distance <= 15 :
    print("Bike")
else :
    print("Car")