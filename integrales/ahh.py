import sympy as s

x = s.symbols('x')
equacion = "(9*x**3)-(2*x**6)" 
# equacion = "15**(1/7)*x**(4/7)" ,(x,4,9)
inte = s.integrate(equacion)
equacion2 = str(inte)
equacion2 = "(-2*(x)**7)/7 + (9*(x)**4)/4"
inte2 = s.integrate(inte ,(x,4,9)).evalf()
print(inte)
print(inte2)