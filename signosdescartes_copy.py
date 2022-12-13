class descartes:
    def pedirvalores():
        x = []
        n = int(input("Ingresa el grado de la operacion "))
        for i in range(n,-1,-1):
            cadena = "Ingresa x" + str(i) + " "
            x.append(float(input(cadena)))
        return x,n
    # Algoritmo para calcular con la ley de signos de Descartes
    def xnegada(x,n):
        xn=[]
        for i in range(0,len(x)):
            if n % 2 == 0:
                if i % 2 == 0:
                    xn.append(x[i])
                else:
                    xn.append(x[i]*-1)
            else: 
                if i % 2 != 0:
                    xn.append(x[i])
                else:
                    xn.append(x[i]*-1)
        return xn
    def signosdescartesfloat(x,n):
        positivos = []
        negativos = []
        complejos = []
        xn = descartes.xnegada(x,n)
        cambios = 0
        print(x)
        # Calcular C?(-x)

        print (xn) 
        # Ciclos para calcular positivos
        for i in range(0, len(x)-1):
            # print(i)
            print(x[i])
            if x[i] == 0:
                print("no",x[i])
                
                if x[i-1] > 0 and x[i+1] < 0 or x[i-1] < 0 and x[i+1] > 0:
                    cambios+=1
                    print("Cambio 1",cambios)
                    print(x[i-1],x[i+1])
                else:
                    print("Sin cambios")
                    print(x[i-1],x[i+1])
                i+=1
            else:
                if x[i] > 0 and x[i+1] < 0 or x[i] < 0 and x[i+1] > 0:
                    cambios+=1
                    print("Cambio 2",cambios)
                    print(x[i],x[i+1])
        for i in range(cambios,-1,-2):
            if i < 0:
                break
            positivos.append(i)
            if len(positivos) <= 1:
                positivos.append(0)
            cambios = 0 
                    
        for i in range(0, len(x)-1):
            # print(i)
            print(xn[i])
            if xn[i] == 0:
                print("no",xn[i])
                
                if xn[i-1] > 0 and xn[i+1] < 0 or xn[i-1] < 0 and xn[i+1] > 0:
                    cambios+=1
                    print("Cambio 1",cambios)
                    print(xn[i-1],xn[i+1])
                else:
                    print("Sin cambios")
                    print(xn[i-1],xn[i+1])
                
            else:
                if xn[i] > 0 and xn[i+1] < 0 or xn[i] < 0 and xn[i+1] > 0:
                    cambios+=1
                    print("Cambio 2",cambios)
                    print(xn[i],xn[i+1])
        for i in range(cambios,-1,-2):
            if i < 0:
                break
            negativos.append(i)
            if len(negativos) <= 1:
                negativos.append(0)
            cambios = 0 
        
        for i in range(0,len(positivos)):
            for j in range(0, len(negativos)):
                if positivos[i] + negativos[j] <= n-1:
                    aa = (n-1)-positivos[i]-negativos[j]
                    print(aa)
                    complejos.append(aa) 
        # print(len(positivos))
        # print(negativos)
        # Ciclo para calcular complejos
        print("Positivos",positivos)
        print("Negativos",negativos)
        print(complejos)
        cad = "POSIBLES  Positivos: " + str(positivos) + " ,Negativos: " + str(negativos) + " ,Complejos: " + str(complejos)
        return cad
     

# signosdescartesfloat()