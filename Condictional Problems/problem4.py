#fruit Ripeness Checker
#Determine If A Fruit Is Ripe ,Overripe,or Unripe Based On Its Color (eg: banana:green-unripe,yellow-ripe,brown-overripe)

fruit = "banana"

color = str(input("Enter A Banana Color :"))
if color == "green":
    print("banana is unripe")
elif color == "yellow":
    print("banana is ripe")
else:
    print("banana is overripe")