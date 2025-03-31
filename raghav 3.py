while True:
    h=int(input("enter a 1 to go and any other no. to end:"))
    if h==1:
        k=5
        n=int(input("enter a no:"))
        i=1
        j=0
        a=5
        while n>=a:
            a=k**i
            m=n//a
            j+=m
            i+=1
            
        else:
            print (j,"is the no. of tralling zeroes in the factorial of",n)
    else:
        break 
        