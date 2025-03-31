while True:
    h=input("enter Y to go and N to end:")
    if h.upper()=="Y":
        num = int(input("enter a number:"))
        if num > 1:
            for i in range(2, (num//2)+1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
    else:
        break
    
