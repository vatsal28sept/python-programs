# Sum Of Even Numbers
# Calculate The Sum Of Even Numbers Up To Given Number n 

n = int(input("Enter the Value Of n : "))
sum_even = 0

for i in range(1,n):
    if i%2==0:
        sum_even += i
print("The Sum Of Even Numbers Is : " , sum_even)