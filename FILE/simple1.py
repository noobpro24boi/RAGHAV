#To find sum of gp
a=int(input("enter first term:"))
r=int(input("enter common ratio:"))
n=int(input("enter the number of terms:"))
sum=a*(((r**n)-1)/(r-1))
print("The sum of gp is:",sum)
