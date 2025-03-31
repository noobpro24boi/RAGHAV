employee=[]
def addition():
     no=int(input("enter employee number:"))
     det=input("enter employee details:")
     final=[no,det]
     employee.append(final)
def deletion():
     employee.pop()

def Display():
    ln = len(employee)
    if len(employee) == 0:
        print("There Are No Books To Show")
    else:
        for i in range(0,ln,1):
            print(employee[i])
while True:
     h=int(input("for addition enter 1, for deletion enter 2 ,for display enter 3 , to end enter 0"))
     if h==1:
          addition()
     elif h==2:
          deletion()
     elif h==3:
          Display()
     elif h==0:
          break
     else:
          print("error")
