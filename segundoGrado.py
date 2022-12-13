class formula_Gen:
    def segundogrado(a,b,c):
        if a != 0:
            d = b**2 -4*a*c
            if d < 0:
                x1r = -b/2*a
                x1i = ((-d)/(2*a))**(1/2)
                x2r = x1r
                x2i = -x1i
            else:
                x1r = (-b+(d)**(1/2))/(2*a)
                x2r = (-b-(d)**(1/2))/(2*a)
                x1i = 0
                x2i = 0
            return x1r,x2r,x1i,x2i
        else:
            if  b == 0:
                if c == 0:
                    print("No hay ecuacion")
                    return 0, 0, 0, 0
                else:
                    print("Ecuacion mal planteada")
                    return 0,0,0,0
            else:
                x1 = -c/b
                print("Ecuacion de primer grado")
                return x1, 0, 0, 0

# x1r,x2r,x1i,x2i = segundogrado(1,-2,2)
# print("X1R:",x1r,"X2R:",x2r,"X1I:",x1i,"X2I:",x2i)