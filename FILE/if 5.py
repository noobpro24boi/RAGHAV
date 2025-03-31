while True:
    k=input("enter no. (yes or no):")
    if k=="yes":
        p=int(input('enter 1st no.:'))
        q=int(input('enter 2nd no.:'))
        h=int(input("enter 1 for adding,2 for subtract,for multiply,5 for devide and 0 for end:"))
        if h==1:
            print(p+q)
        elif h==2:
            print(p-q)
        elif h==3:
            print(p*q)
        elif h==4:
            print(p/q)
        elif h==0:
            break
    if k=="no":
        break
