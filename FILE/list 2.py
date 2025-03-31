income=int(input("enter monthly income:"))
expenditure=[]
i=0
while i<12:
    expenditure1=int(input("enter your expenditure of the month:"))
    expenditure.append(expenditure1)
    i=i+1
sum1=0
for j in expenditure:
    sum1+=j
print("your monthly expenditure is ",(sum1/12),"approx" )
k=12*(income)-sum1
print("your total saveing:",k)
