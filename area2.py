def areas():
    a=int(input("enter side of square"))
    return a*a
def arear():
    l=int(input("enter side of rectangle"))
    b=int(input("enter side of rectangle"))
    return l*b

def areac():
    r=int(input("enter radius of circle"))
    return (22/7)*r*r
def areat():
    s=int(input("side1:"))
    t=int(input("side2:"))
    u=int(input("side3:"))
    g=(s+t+u)/2
    return ((g)*(g-s)*(g-t)*(g-u))**(1/2)
while True:
    print("enter 1 for square 2 for rectangle 3 for circle 4 for triangle")
    ch=int(input("enter choice"))
    if(ch==1):
        print(areas())
    elif(ch==2):
        print(arear())
    elif(ch==3):
        print(areac())
    elif(ch==4):
        print(areat())
    else:
        print("not a avlid choice")
    c1=input("enter Y for ending the loop")
    if(c1=="Y"):
        break
