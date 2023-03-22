
def incomodam(n, i=0, texto=""):
    if (n == i):
        return texto
    elif (n > i):
        return texto + "incomodam " + incomodam(n, i=i+1, texto=texto)
    else:
        return ""


def elefantes(n, i=1, texto=""):
    if n > i:
        if i == 1:
            return texto + "Um elefante incomoda muita gente\n" + elefantes(n, i+1)
        else:
            return texto + str(i) + " elefantes " + incomodam(i) + "muito mais\n" + str(i) + " elefantes incomodam muita gente\n" + elefantes(n, i+1)
    else:
        return texto + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
