#Programa que calcula la recta dado unos puntos en x & y usando el metodo de minimos cuadrados
from sympy import *
import gauss
import numpy as np
import sys


class minicuadra:
    def lineal(x,y): #x & y son arrays
        n = len(x)
        xy = 0
        xa = 0
        ya = 0
        x2 = 0
        for i in range(n):
            xy = xy + x[i] * y[i]
            x2 = x2 + x[i] * x[i]
            xa = xa + x[i]
            ya = ya + y[i]
        a0 = (x2*ya-xa*xy)/(n*x2-xa*xa)
        a1 = (n*xy- xa*ya)/(n*x2-xa*xa)
        return a0, a1

    def polinomica(x,y):
        n = len(x)
        xa = 0
        ya = 0
        x2 = 0
        x3 = 0 
        x4 = 0
        xy = 0
        x2y = 0
        for i in range(n):
            xa += x[i]
            ya += y[i]
            x2 += x[i] * x[i]
            x3 += x[i] * x[i] * x[i]
            x4 += x[i] * x[i] * x[i] * x[i]
            xy += x[i] * y[i]
            x2y += x[i] * x[i] * y[i]
        a = np.array([[n,xa,x2,ya],[xa,x2,x3,xy],[x2,x3,x4,x2y]])
        ar = gauss.gaussjordan.gauss(3,4,a)
        a0 = ar[0,3]
        a1 = ar[1,3]
        a2 = ar[2,3]
        return a0, a1, a2

    def pedirDatos():  #En consola
        x = []
        y = []
        n = int(input("Cantidad de datos> "))
        for i in range(n):
            cadena = "Posicion en x del punto" + str(i+1) + "> "
            aux = float(input(cadena))
            x.append(aux)
            cadena = "Posicion en y del punto" + str(i+1) + "> "
            aux = float(input(cadena))
            y.append(aux)
        return x, y

# x,y = pedirDatos()   

def main():
    x = [1,2,3,4,5,6,7]
    y = [4,7,9,10,9,7,4]
    print(x)
    print(y)
    a0, a1 = minicuadra.lineal(x,y)
    print(a0)
    print(a1)
    a0, a1, a2 = minicuadra.polinomica(x,y)
    print(a0)
    print(a1)
    print(a2)

if __name__ == '__main__':
    sys.exit(main())