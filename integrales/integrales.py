from sympy import *
class integrales:
    

    def integral(f,a,b):
        x = symbols("x")
        return integrate(f,(x,a,b)).evalf()

# f = input("Ecuacion> ")
# a = float(input("Limite inferior> "))
# b = float(input("Limite superior> "))

# p = integral(f,a,b)
# print(p)