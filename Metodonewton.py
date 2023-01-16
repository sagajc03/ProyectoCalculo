#Metodo Newton-Rapshon

from math import fsum
from decimal import Decimal

class newthon_r:
    def pedirvalores():
        x = []
        n = int(input("Ingresa el grado de la operacion "))
        for i in range(n,-1,-1):
            cadena = "Ingresa x" + str(i) + " "
            x.append(Decimal(float(input(cadena))))
        return x,n
    def nwtonrap(x,x12,x11,x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0):
        
        try:
            fx = Decimal(fsum([x12*x**12,x11*x**11,x10*x**10,x9*x**9,x8*x**8,x7*x**7,x6*x**6,x5*x**5,x4*x**4,x3*x**3,x2*x**2,x1*x**1,x0]))
            dfx = Decimal(fsum([(x12*12*x**11),(x11*11*x**10),(x10*10*x**9),(x9*9*x**8),(x8*8*x**7),(x7*7*x**6),(x6*6*x**5),(x5*5*x**4),(x4*4*x**3),(x3*3*x**2),(x2*2*x**1),x1]))
            y = Decimal(fsum([x , -fx/dfx]))
            for i in range(1,1000):
                x = y
                fx = Decimal(fsum([x8*x**8,x7*x**7,x6*x**6,x5*x**5,x4*x**4,x3*x**3,x2*x**2,x1*x**1,x0]))
                dfx = Decimal(fsum([(x8*8*x**7),(x7*7*x**6),(x6*6*x**5),(x5*5*x**4),(x4*4*x**3),(x3*3*x**2),(x2*2*x**1),x1]))
                y = Decimal(fsum([x , -fx/dfx]))
            return x, fx
        except:
            print("division entre 0")
            return Decimal(1), Decimal(0)

            
    def definir(x,n):
        x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = (Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0))
        if n > 12:
            print("Demasiado largo")
        x0 = x[n]
        if n > 0:
            x1 = x[n-1]
        if n > 1:
            x2 = x[n-2]
        if n > 2:
            x3 = x[n-3]
        if n > 3:
            x4 = x[n-4]
        if n > 4:
            x5 = x[n-5]
        if n > 5:
            x6 = x[n-6]
        if n > 6:
            x7 = x[n-7]
        if n > 7:
            x8 = x[n-8]
        if n > 8:
            x9 = x[n-9]
        if n > 9:
            x10 = x[n-10]
        if n > 10:
            x11 = x[n-11]
        if n > 11:
            x12 = x[n-12]
    
        return x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12


    def definir2(x,n):
        x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = (Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0),Decimal(0.0))
        if n > 12:
            print("Demasiado largo")
        x0 = Decimal(x[0])
        if n > 0:
            x1 = Decimal(x[1])
        if n > 1:
            x2 = Decimal(x[2])
        if n > 2:
            x3 = Decimal(x[3])
        if n > 3:
            x4 = Decimal(x[4])
        if n > 4:
            x5 = Decimal(x[5])
        if n > 5:
            x6 = x[6]
        if n > 6:
            x7 = x[7]
        if n > 7:
            x8 = x[8]
        if n > 8:
            x9 = x[9]
        if n > 9:
            x10 = x[10]
        if n > 10:
            x11 = x[11]
        if n > 11:
            x12 = x[12]
    
        return x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
    


# x = 1
# xe = Decimal(0.0)
# fx = Decimal(0.0)
# e,n = pedirvalores()
# x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12 = definir(e,n)
# for i in range(-100,100):
#     aux1=xe
#     aux2=fx
#     auxstr = str(xe)
#     xe,fx = nwtonrap(x+i*x,x12,x11,x10,x9,x8,x7,x6,x5,x4,x3,x2,x1,x0)
#     xstr = str(xe)
#     if(xstr != auxstr):
#         print("Raiz",xe)


