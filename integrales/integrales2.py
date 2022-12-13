import math as m

def traductor(x):
    y = (m.sin(9*x**2-3*x)**5)**3
    return y


def integralA(limI,limF):
    n = 10000
    h = (limF - limI)/n
    xi = limI
    xf = xi + h
    yi = traductor(xi)
    yf = traductor(xf)
    ar = (yf+yi)/2*h #Area
    for i in range(n-1):
        xi += h
        xf += h
        yi = traductor(xi)
        yf = traductor(xf)
        ar += (yf+yi)/2*h
    return ar

limI = int(input("Limite Inferior "))
limF = int(input("Limite Superior "))
print(integralA(limI,limF))