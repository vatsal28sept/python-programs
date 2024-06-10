#cofee customization
#customise a coffe order: "small","medium" or "large"n with an opetion for "Extra shot" of expresso

order_size = "medium"
extra_shotv = True

if extra_shotv:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"

print("Order : " ,coffee)