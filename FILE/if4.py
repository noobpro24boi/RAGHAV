d=int(input("enter a number:"))
if d%2==0:
    print("It is divisible by 2")
if d%3==0:
    print("It is divisible by 3")
if d%5==0:
    print("It is divisible by 5")
if d%2!=0 and d%3!=0 and d%5!=0:
    print("The number is not divisible by 2,3 or 5")
