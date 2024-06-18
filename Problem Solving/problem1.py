# How To Find Average Of N Numbers \

num = int(input("How Many Numbers ?"))
total_sum = 0
for i in range(num):
    numbers = float(input("Enter Number :"))
    total_sum += numbers

avg = total_sum / num
print("Average Is : ",avg)
