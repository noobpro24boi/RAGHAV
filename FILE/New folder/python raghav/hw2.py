i=int(input("no."))
s=2
if i<=1:
    print("wrong no.")
elif i==2:
    print("the no. 2 is a prime no.")
else:
    while(s<i):
        g=i%s
        s+=1
        if g==0:
            break
    if g==0:
        print("the no.",i,"is a composite number")
    else:
        print("the no",i,"is a prime number")     
