# Password Strength Checker 
# check if pasword id "weak","medium",or "strong". criteria: <6 char(weak),6-10 char(medium),>10(strong)

password = input("Enter Your Password: ").strip()  # Strip any leading or trailing spaces

# print(f"Debug: Password length is {len(password)}")  # Debug statement to check the length

if len(password) < 6:
    print("Your Password Strength Is Weak")
elif len(password) <= 10:
    print("Your Password Strength Is Medium")
else:
    print("Your Password Strength Is Strong")


