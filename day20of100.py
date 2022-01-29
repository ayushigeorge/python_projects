#DAY 20 OF 100 
#FACTORIAL PROGRAMME

num = int(input("Enter a number for its factorial: "))
fact = 1;
if num>=1:
    for i in range (1, num+1):
        fact = fact*i;

print("Factorial of ",num, "is: ", fact)
    



