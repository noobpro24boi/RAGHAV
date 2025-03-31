def bubblesort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                no=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=no
list1=[]
l=0
k=int(input('no. of elements in list:'))
for l in range(0,k):
    m=int(input("enter element of list:"))
    list1.append(m)
print ("original list is:",list1)
bubblesort(list1)
print ("sorted list is:",list1)
