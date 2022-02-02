#Day 24 of 100
#To discplay Fibonacci Series of the given number


def Fibonacc_series(n):
    
    if n<0:
        print("Invalid number!")
    elif n==0:
        return(0)
    elif n==1:
        return(1)
    else :
        return(Fibonacc_series(n-1)+ Fibonacc_series(n-2))

        
print("13th element of Fibonacci series: ",Fibonacc_series(13))
