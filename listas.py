def lista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if 8 in lista1:
        print("8 está na linha")
    else:
        print()


def sortlista():
    lista1 = [5, 2, 4, 6, 2, 4, 2, 1, 6, 7, 4, 9, 123, 5, 9]
    print(lista1)
    lista1.sort()
    print(lista1)


def countlista():
    lista1 = [2, 4, 5, 6, 4, 3, 5, 6, 2]
    print(lista1.count(3))


def appendlista():
    lista1 = [2, 5, 4, 2, 5, 6, 2, 1, 3]
    print(lista1)
    lista1.append([20, 4, 5, 2])
    print(lista1)


def extendlista():
    lista1 = [2, 5, 4, 2, 5, 6, 2, 1, 3]
    print(lista1)
    lista1.extend([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(lista1)


def insertlista():
    lista1 = [2, 5, 4, 2, 5, 6, 2, 1, 3]
    print(lista1)
    lista1.insert(2, 240)
    print(lista1)


def juntarlista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lista3 = lista1 + lista2
    print(lista1)
    print(lista2)
    print(lista3)

    lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista4)
    lista5 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(lista5)
    lista4 = lista4 + lista5
    print(lista4)


def reverselista():
    lista1 = [5, 2, 4, 6, 2, 4, 2, 1, 6, 7, 4, 9, 123, 5, 9]
    print(lista1)
    lista1.reverse()
    print(lista1)

def reversesortlista():
    lista1 = [5, 2, 4, 6, 2, 4, 2, 1, 6, 7, 4, 9, 123, 5, 9]
    print(lista1)
    lista1.sort()
    lista1.reverse()
    print(lista1)

def copiarlista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = lista1.copy()

    print(lista1)
    print(lista2)

    lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista4 = lista3
    print(lista3)
    print(lista4)

def contarlista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(lista1)
    print(len(lista1))

def poplista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lista3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    lista4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


    print(lista1)
    lista1.pop()
    print(lista1)

    print(lista2)
    print(lista2.pop())
    print(lista2)

    print(lista3.pop())

    print(lista4)
    print(lista4.pop(2))
    print(lista4)

def clearlista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista1)
    lista1.clear()
    print(lista1)

def multilista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = lista1 * 3
    print(lista1)
    print(lista2)

def splitlista():
    a = "Eu gosto de comida"
    b = a.split()
    print(a)
    print(b)

    c = "Eu,gosto,de,comida"
    d = c.split(",")
    print(c)
    print(d)

def joinlista():
    lista1 = ["Eu", "gosto", "de", "comida"]
    a = " ".join(lista1)
    print(lista1)
    print(a)

    lista2 = ["Eu", "gosto", "de", "comida"]
    b = "%".join(lista1)
    print(lista2)
    print(b)

def forlista():
    soma = 0
    total = ""

    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = ["P", "e", "d", "r", "o"]

    for elemento in lista1:
        print(elemento)

    for elemento in lista1:
        soma = soma + elemento
    print(soma)

    for elemento in lista2:
        total = total + elemento

    print(total)

def whilelista():
    lista1 = []
    produto = ''
    while produto != "sair" :
        produto = input()
        if produto != "sair":
            lista1.append(produto)

    for produto in lista1:
        print(produto)

def variavellista():

    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    num5 = 5

    lista1 = [num1, num2, num3, num4, num5]

    print(lista1)

def indexlista():

    cores = ["amarelo", "verde", "azul", "vermelho", "branco"]

    print(cores[0])
    print(cores[1])
    print(cores[2])
    print(cores[3])
    print(cores[4])
    print()
    print(cores[0])
    print(cores[-1])
    print(cores[-2])
    print(cores[-3])
    print(cores[-4])

def enumeratelista():
    cores = ["amarelo", "verde", "azul", "vermelho", "branco"]
    for indice, cor in enumerate(cores):
        print(indice, cor)

def knowindicelista():
    cores = ["amarelo", "verde", "azul", "vermelho", "branco", "amarelo"]
    print(cores.index("amarelo")) #apenas o primeiro indice
    print(cores.index("amarelo", 1)) #apenas o primeiro indice

def slicinglista():
    cores = ["amarelo", "verde", "azul", "vermelho", "branco"]
    print(cores[1:3])
    lista1 = ["Pedro", "Marco"]
    print(lista1)
    lista1[0], lista1[1] = lista1[1], lista1[0]
    print(lista1)

def somamaxminlista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(lista1))
    print(max(lista1))
    print(min(lista1))
    print(len(lista1))

def transtuplalista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista1)
    print(type(lista1))

    tupla = tuple(lista1)
    print(tupla)
    print(type(tupla))

def unpacklista():
    lista1 = [1, 2, 3]
    lis1, lis2, lis3 = lista1
    print(lis1)
    print(lis2)
    print(lis3)

def shallowanddeepcopylista():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista1)
    nova = lista1.copy()
    print(nova)
    nova.append(11)

    print(lista1)
    print(nova)

    print()

    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nova2 = lista2

    print(lista2)
    print(nova2)
    nova2.append(11)
    print(lista2)
    print(nova2)

shallowanddeepcopylista()