t=()
k=int(input("no. of integers :"))
for i in range(0,k):
    m=int(input("enter a no.:"))
    t+=(m,)
print(t)
m=max(t)
j=min(t)
print("max-min=",(m-j))
