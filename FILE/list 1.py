shopping_list=[]
cost=[]
sum1=0
while True:
    item=input("enter item for shopping,to end enter 'done':")
    if item!="done":
        shopping_list.append(item)
        cost1=int(input("enter cost of item:"))
        cost.append(cost1)
    elif item=="done":
        break
for i in cost:
    sum1+=i
print("list:",shopping_list)
print("total cost:",sum1)
