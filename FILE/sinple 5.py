print("""Quadratic Equation is
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0""")
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
d = (b**2) - (4*a*c)
sol1 = (-b-(d**0.5))/(2*a)
sol2 = (-b+(d**0.5))/(2*a)
print('The solution are',sol1,"and",sol2)
