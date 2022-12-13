import itertools

#Teorema sobre las raices racionales de una ecuacion algebraica de coeficientes enteros
class CoeficioentesEnteros:
    def factorizar(n):
        resultado = []
        if n < 0:
            n = n*-1
        for i in range(1,n+1):
            if n % i == 0:
                resultado.append(i)
        if resultado == []:
            resultado.append(1)
        return resultado

    def raices(factorizacion1,factorizacion2):
        a =  itertools.product(factorizacion1,factorizacion2,repeat=1)
        return a

