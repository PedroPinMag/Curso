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

insertlista()
