#Pet Food Recomendation 
# Recomended A Type Of Pet Food Based On The Pet's Species And Age(eg:Dog<2years-puppy food, Cat:>5Senior Cat Food)

species = input("Enter the species of your pet : ").strip().lower()
age = int(input("Enter the age of your pet in years: "))

if species == "dog":
    if age < 2:
        print("Recommended Food: Puppy Food")
    elif age >= 2 and age <= 7:
        print("Recommended Food: Adult Dog Food")
    else:
        print("Recommended Food: Senior Dog Food")
elif species == "cat":
    if age < 1:
        print("Recommended Food: Kitten Food")
    elif age >= 1 and age <= 7:
        print("Recommended Food: Adult Cat Food")
    else:
        print("Recommended Food: Senior Cat Food")
else:
    print("Sorry, we don't have recommendations for that species.")
