import numpy as np
# import sys

class gaussjordan:
    def gauss(n,m,a):
        for i in range(0,n):
            pivote = a[i,i]
            for j in range(i,m):
                a[i,j] = a[i,j]/pivote
            for k in range(0,n):
                if k != i:
                    cero = a[k,i]
                    for j in range(i,m):
                        a[k,j] = a[k,j]-cero*a[i,j]
                    continue
                else:
                    continue
            continue
        return a



    def tomardatos(n):
        m = n+1
        a = np.zeros((n,m))
        for i in range(0,n):
            for j in range(0,m):
                cadena = "ingresa el valor de" , i ,j
                a[i,j] = int(input(cadena))

        return a


# def main():
#     n = int(input("Tamaño"))
#     a = gaussjordan.tomardatos(n)
#     print(a)
#     a = gaussjordan.gauss(n,n+1,a)
#     print(a)


# if __name__ == '__main__':
#     sys.exit(main())