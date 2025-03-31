d={}
for i in range(0,2900,400):
    k=i+100
    l=i+200
    m=i+300
    d[i]=6
    d[k]=4
    d[l]=2
    d[m]=0
n=int(input("enter date:"))
o=int(input("enter year:"))
s=int(input("enter month no. (eg- for january month no. is 1):" ))
k={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
p=o%100
q=(o//100)*100
r=p//4
t=int(k[s])
u=int(d[q])
v=(u+t+r+p+n)

if s<=2 and o%4==0:
    v=v-1
w=v%7
x={0:"sunday",1:"monday",2:"tuesday",3:"wednesday",4:"Thursday",5:"friday",6:"Saturday"}
y=x[w]
print("your birthday was on:",y)
