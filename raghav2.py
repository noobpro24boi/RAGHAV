s=int(input("enter no. of sides Polygon(should be):"))
sum=(s-2)*180
print ("sum of all angles is",sum)
l=[]
j=0
for i in range (0,s):
    r=int(input("enter ratio of  angle:"))
    l.append(r)
    j+=r
x=sum/j
v=1
for k in l:
    m=k*x
    print("angle ",v,"is",m)
    v=v+1
    