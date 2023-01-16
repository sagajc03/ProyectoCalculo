class utilidades:
    def separarTerminos(polinomio:str):

        # quitar los space
        polinomio = polinomio.replace(' ','')

        terminoActual = ''
        terminos = []
        numeroParentesis = 0

        # Por cada caracter en polinomio
        for i in range(len(polinomio)):
            caracterActual = polinomio[i]

            # El primero caracter, siempre se agrega a terminoActual
            if i == 0:
                terminoActual = terminoActual + caracterActual

            # El ultimo caracter
            elif i == len(polinomio) - 1:
                terminoActual = terminoActual + caracterActual
                terminos.append(terminoActual)

            # Otros caracteres
            else:

                # Si se encuentra parentesis, actualizamos el valor de numeroParentesis
                if caracterActual == '(':
                    numeroParentesis += 1
                    terminoActual = terminoActual + caracterActual
                elif caracterActual == ')':
                    numeroParentesis -= 1
                    terminoActual = terminoActual + caracterActual

                # Si se encuentra operador '+' o '-'
                elif caracterActual == '+' or caracterActual == '-':

                    # Si estamos dentro de parentesis
                    if numeroParentesis > 0:
                        terminoActual = terminoActual + caracterActual

                    # Si estamos fuera de parentesis, crea un nuevo termino
                    else:
                        terminos.append(terminoActual)
                        terminoActual = caracterActual

                # Otros caracteres
                else:
                    terminoActual = terminoActual + caracterActual

        return terminos

