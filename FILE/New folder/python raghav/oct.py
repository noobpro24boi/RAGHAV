while True:
    q=int(input("1 to go,any other no. to break: ") )
    if (q==1):
        g=float(input("enter floating no.:"))
        k=int(g)
        t=(oct(k)[2:])
        s=(g-k)*8
        print()
        if s==0:
            print(t)
            break
        else:
            h=int(s)
        l=(s-h)*8
        if l==0:
            print(t,".",h)
            break
        else:
            d=int(l)
        a=(l-d)*8
        if a==0:
            print(t,".",h,d)
            break
        else:
            n=int(a)
        j=(a-n)*8
        if j==0:
            print(t,".",h,d,n)
            break
        else:
            m=int(j)
            print(m)
        print(t,".",h,d,n,m)
    else:
        break
    


