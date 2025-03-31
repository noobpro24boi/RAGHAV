while True:
    s=2
    h=int(input("1to go,0to break"))
    if h==0:
            break
    if h==1:
        i=int(input("no."))
        if i<=1:
            print("wrong no.")
        elif i==2:
            print("the no",i,"is a prime number")
        else:
            while(s<i):
                g=i%s
                s+=1
                if g==0:
                    break
            if g==0:
                print("the no.",i,"is a composite number")
                print("the no. ",(s-1),"is least factor of the no.",i)
            else:
                print("the no",i,"is a prime number")
        


