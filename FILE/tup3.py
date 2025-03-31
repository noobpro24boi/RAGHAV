t=()
k=int(input("no. of integers :"))
for i in range(0,k):
    m=int(input("enter a no.:"))
    t+=(m,)
print(t)
t2=sorted(t)
print(t2)
for i in range(0,k):
    k=" "*i
    print(k,t2[i])
