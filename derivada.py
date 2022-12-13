import numpy as np
class derivada:
    def pedirfx(n):
        a = np.zeros((2,n))
        for i in range(0,n):
            cadena2 = "Escribe el valor del exponente del polinomio " + str(i+1) + " : "
            a[0,i] = int(input(cadena2))
            cadena1 = "Escribe el valor del polinomio " + str(i+1) + " : " 
            a[1,i] = int(input(cadena1))
        return a ,n 

    def sacarfxalt(a,n,x):
        fx = 0
        for i in range(0,n):
            fx = a[1,i]*(x)**a[0,i] + fx
        return fx

    def sacarfx(a,n,x):
        fx = 0
        for i in range(0,n+1):
            fx = a[n-i]*(x)**(i) + fx
        return fx

    def sacarmatdfx(a,n):
        adfx = a
        for i in range(0,n):
            adfx[1,i] = adfx[1,i]*adfx[0,i]
            adfx[0,i] = adfx[0,i] - 1
        return adfx

    ########################################################
    def sacardfx(a,n,x):    #a = vector,n = grado de la operacion, x = lugar en el plano
        adfx = [] 
        for i in range(0,n):
            adfx.append(a[i]*(n-i))
        dfx = 0
        for i in range(0,n):
            dfx = adfx[n-1-i]*(x)**(i) + dfx
        return adfx, dfx
    def scardfxalt(a,n,x):
        h1 = 0.00000001
        h2 = -0.00000001
        dfx1 = (derivada.sacarfxalt(a,n,x+h1)-derivada.sacarfxalt(a,n,x))/h1
        dfx2 = (derivada.sacarfxalt(a,n,x+h2)-derivada.sacarfxalt(a,n,x))/h2
        dfx = (dfx1+dfx2)/2
        return dfx
    def dfxalt(a,n,x):
        h1 = 0.0000001
        h2 = -0.0000001
        dfx1 = (derivada.sacarfx(a,n,x+h1)-derivada.sacarfx(a,n,x))/h1
        dfx2 = (derivada.sacarfx(a,n,x+h2)-derivada.sacarfx(a,n,x))/h2
        dfx = (dfx1+dfx2)/2
        return dfx

# a = [4,0,0,0]
# fx = sacarfx(a,len(a)-1,1)
# adfx, dfx = sacardfx(a,len(a)-1,1)
# print(a)
# print(fx)
# print(adfx)
# print(dfx)
# aldfx = dfxalt(a,len(a)-1,1)
# print(aldfx)

# a ,n = pedirfx()
# print(a)
# fx = sacarfxalt(a,n,1)
# dfx = scardfxalt(a,n,1)
# adfx = sacarmatdfx(a,n)

# print(fx)
# print(dfx)
# print(adfx)