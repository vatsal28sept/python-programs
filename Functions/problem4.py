# Function Returning Multiple Values 
# Create A Function That Returns Both The Area And Circumference of a circle given its radius

import math
def circle_status():
    radius = int(input("Enter The Value Of Radius : "))
    area = math.pi * radius ** 2
    circ = 2 * math.pi * radius
    return area,circ
a,c = circle_status()
print("Area : " , a , "Circumference : " , c)