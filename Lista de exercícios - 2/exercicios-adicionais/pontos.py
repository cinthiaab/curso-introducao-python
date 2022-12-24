x1 = int(input("Insira a coordenada x do primeiro ponto: "))
y1 = int(input("Insira a coordenada y do primeiro ponto: "))
x2 = int(input("Insira a coordenada x do segundo ponto: "))
y2 = int(input("Insira a coordenada y do segundo ponto: "))

d = ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2)

if(d<10):
    print("perto")
else:
    print("longe")