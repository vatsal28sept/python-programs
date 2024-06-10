# Grad Calculator
# Assign A Letter Gard Based On Student's Score : A(90-100) ,B (80-89) , C (70-79) , D (60-69) , F (below 60)

marks = int(input("Enter Students Marks : "))

if marks > 100:
    print("Your Are Enter Wrong Details")
    exit()
elif marks>=90 and marks<=100:
    print("Student's Score Is A Gard")
elif marks>=80 and marks<=89:
    print("Student's Score Is B Grad")
elif marks>=70 and marks<=79:
    print("Student's Score Is C Grad")
elif marks>=60 and marks<=69:
    print("Student's Score Is D Grad")
else:
    print("Student Is Fail")