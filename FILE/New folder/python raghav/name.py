"""n tak factorial
no. revers without string"""

n=int(input("no."))
f=1
for i in range(2,n+1,1):
    for j in range(1,i,1):
        s=i*j
        f=s*((i-1)*(j-1))
    
    if i>3:
        print(f)
    else:
        print(s)
         
