# Movie Ticket Pricing
# Movie Ticket Are Priced Based On Age : $12 for Adults(18 And Over), $8 For Children ,Everyone Gets A $2 Discoumt On Wednesday

age = int(input("What Is Your Age?: "))
day = str(input("Enter A Day: "))
if age >= 18 :
    price = 12
   
else:
    price = 8
   
if day == "wednesday" :
    price -= 2
    print("You Got A Wednesday Discount Of $2 ")

print("Give Me $" + str(price) + " And Get Your Ticket")