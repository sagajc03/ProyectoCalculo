#Programa para calcular una raiz de una ecuacion algebraica con el metodo de newton
#de segundo orden (triple division sintetica)

def divisionsintetica(n,x):
    a = [] 
    b = [] 
    if n >= 2:
        m = n + 1
        for i in range(0,m):
            a.append(float(input()))
        b.append(a[0])
        for i in range(1,m):
            b.append(a[i] + x*b[i-1])
        return b

n = int(input("Grado de la operacion "))
x = float(input("Numero a evaluar "))
print(divisionsintetica(n,x))