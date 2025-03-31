a =int(input("enter 1st side:"))
b =int(input("enter 2nd side:"))
c =int(input("enter 3rd side:"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is',area)
