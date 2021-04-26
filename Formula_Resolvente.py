## Formula Resolvente ##
from math import *

# Input and integer

print("\nFórmula: ax^2 + bx + c = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Calculation

d = (b**2) - (4*a*c)

sol1 = (-b-sqrt(d))/(2*a)
sol2 = (-b+sqrt(d))/(2*a)

# Result

print("\nResultados:")
print("x1 = " + str(sol1))
print("x2 = " + str(sol2))
