# Find The First Non-Repeated Character 
# Given A String ,Find The First Non-Repeated Character

name = str(input("Enter The Value Of String : "))
for char in name:
    if name.count(char) == 1:
        print("Non-Reapeted Char Is : ",char)