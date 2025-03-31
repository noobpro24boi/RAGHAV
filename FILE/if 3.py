a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
c=float(input("Enter 3rd number:"))
if b<a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
if a<b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)
if b<c>a:
    if b>a:
        print(c,b,a)
    else:
        print(c,a,b)
if a==b==c:
    print("1st number(",a,")=","2nd number(",b,")=3rd number(",c,")")
