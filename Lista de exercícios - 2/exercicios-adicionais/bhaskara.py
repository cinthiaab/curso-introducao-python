a = float(input("Insira o parametro a: "))
b = float(input("Insira o parametro b: "))
c = float(input("Insira o parametro c: "))

delta = b**2 - 4*a*c

if (delta > 0):
    x = (-b + delta**(1/2))/2*a
    y = (-b - delta**(1/2))/2*a
    if (x == y):
        print("a raiz dupla desta equação é" + str(x))
    else:
        if (x < y):
            print("as raízes da equação são " + str(x) + " e " + str(y))
        else:
            print("as raízes da equação são " + str(y) + " e " + str(x))
elif (delta == 0):
    x = (-b + delta**(1/2))/2*a
    print("a raiz desta equação é " + str(x))
else:
    print("esta equação não possui raízes reais")
