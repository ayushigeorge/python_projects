#DAY 19 0F 100
#TO FIND IF NUMBER IS PALLINDRONE OR NOT IN PYTHON

#taking input
num =int(input("Enter a number to check if its pallindrone or not: "))
#initialise the value
temp =num
rev = 0
#using while loop
while temp !=0:
    digit = rev*10
    rev = temp %10 +digit
    temp = temp// 10

if num ==rev:
    print("The number is pallindrone.")
else:
    print("the number is not a pallindrone number.")

