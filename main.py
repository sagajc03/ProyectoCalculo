from BinomioNewton import BinomioNewton 
from coeficientesEnteros import CoeficioentesEnteros
from gauss import gaussjordan
from derivada import derivada
# print(BinomioNewton.binomionew(18))


# f1 = CoeficioentesEnteros.factorizar(10)
# f2 = CoeficioentesEnteros.factorizar(10)

# a = CoeficioentesEnteros.raices(f1,f2)
# pool=[f1,f2]
# lista = []

# for n in a:
#       lista.append(n)

# print(lista)

n = int(input("Numero de polinomios"))
a,n = derivada.pedirfx(n)
print(a)
fx = derivada.sacarfxalt(a,n,1)
dfx = derivada.scardfxalt(a,n,1)
adfx = derivada.sacarmatdfx(a,n)

print(fx)
print(dfx)
print(adfx)