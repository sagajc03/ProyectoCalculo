import sympy as s

global parentesis
contador = 0 

#cadena.find('ha') # 'ha' no está en 'hola', find() retorna -1

def buscarTrigo(equacion): #busca por cualquiera de sin, csc, sec, tan, cot, asin, acsc, acos, asec, atan, acot, atan2
    lista = []
    pos_inicial = -1
    try:
        while True:
            pos_inicial = equacion.index('sin',pos_inicial+1)
            lista.append(pos_inicial)
    except ValueError:
        return lista

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def parentesisLug(equacion,places):
    lista = []
    pc = equacion.count("(")
    for i in range(pc):
        equacion = equacion[places[i]:]
        lista.append(find_between(equacion,'(',')'))
    return lista

def resolverEq(equacion):
    lugares = buscarTrigo(equacion)
    dentro = parentesisLug(equacion,lugares)
    s = s.symbols('s')
    


x = s.symbols('x')
equacion = "10 + sin(x+1)"




lugares = buscarTrigo(equacion)
print(lugares)
a = parentesisLug(equacion,lugares)
print(a)
eq1 = s.sympify(a[0])
eq1 = eq1.replace(x,5)
print(eq1)

# texto = "sin(sin(x+1))"
# esta, pos = buscaTexto("sin",3,texto,len(texto))
# print(pos) #12

# x = s.symbols('x')
# cadena = "sin(sin(x+1))"
# eq1 = s.sympify(cadena)
# eq1 = eq1.replace(x,5)
# cadena2 = str(eq1)

# print(eq1) #35
# print(cadena2)