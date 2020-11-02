from sympy import symbols
from sympy import sqrt
from sympy import expand,factor

# the variables are defined using the symbols 
# variables must be defined before they are used by us.
x,y = symbols('x y')
expr = x+2*y
print(expr)
print(expr - y)
print(x*(x+2*y))
print(sqrt(8))

print(expand(x*expr))
print(factor(expand(x*expr)))
