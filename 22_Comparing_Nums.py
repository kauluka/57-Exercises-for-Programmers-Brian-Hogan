# 22. Comparing Numbers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

largest_num = 0 

if num1 >= num2 and num3:
    largest_num = num1
elif num2 >= num1 and num3:
    largest_num = num2
else:
    largest_num = num3
print("The largest number is ", largest_num, ".", sep='')