from sympy import *

# integrate(f, var)

x = symbols("x")
y = symbols("y")
f = sqrt(2*x*y +1)
p = integrate(f, x)

# integrate(f, (var,a,b))
f = x
a = symbols("a")
b = symbols("b") 
p = integrate(f , (x,a,b))

f = x**4 * sin(x)

p = integrate(f, (x, 0, pi/3)).evalf()

print(p)

