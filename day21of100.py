#Day 21 of 100 
# Armstrong Number Programme

num = int(input("enter a number to check its Armstrong number or not: "))

#initialising the sum and temperory variable to store original value of number
sum = 0

temp = num
while temp>0:
    
    dig =temp %10
    sum = sum + dig ** 3 
    temp= temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

