#Day 31 of 100 days of code
#Reversing Number


num = int(input("Enter a number: "))
reverse = 0

while num>0:
    rem = num%10
    reverse = reverse *10 + rem
    num = num//10
    
print("the reverse number is: {}".format(reverse))