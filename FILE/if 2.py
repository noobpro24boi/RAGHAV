while True:
    q=int(input("1 to go,any other no. to break: ") )
    if (q==1):
        g=float(input("enter floating no.:"))
        k=int(g)
        t=(bin(k)[2:])
        s=(g-k)*2
        print()
        if s==0:
            print("bin. number:",t)
            break
        else:
            h=int(s)
        l=(s-h)*2
        if l==0:
            print("bin. number:",t,".",h)
            break
        else:
            d=int(l)
        a=(l-d)*2
        if a==0:
            print("bin. number:",t,".",h,d)
            break
        else:
            n=int(a)
        j=(a-n)*2
        if j==0:
            print("bin. number:",t,".",h,d,n)
            break
        else:
            m=int(j)
        print("bin. number:",t,".",h,d,n,m)
    else:
        break
