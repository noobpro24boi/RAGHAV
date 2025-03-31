list1=[]
list2=[]
list3=[]
le=int(input("no. of elements in list"))
for i in range(0,le+1):
    h=int(input("enter a no."))
    list1.append(h)
for i in list1:
    if i%2==0:
        list2.append(i)
    elif i%2!=0:
        list3.append(i)
print(list1)
print(list2)
print(list3)
