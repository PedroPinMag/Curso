def tipotupla():
    print(type(()))


def tupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tupla1)
    tupla2 = 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    print(tupla2)

def tuplascomumelemento():
    tupla1 = (1,)
    a = 1
    print(tupla1)
    print(a)

def tuplascomrange():
    tupla1 = tuple(range(1))
    print(tupla1)

def sumtupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(sum(tupla1))

def maxtupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(max(tupla1))

def mintupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(min(tupla1))

def lentupla():
    tupla1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(len(tupla1))

def concatencaotuplas():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tupla2 = 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    tupla3 = (tupla1 + tupla2)
    print(tupla1 + tupla2)
    print(tupla1)
    print(tupla1)
    print(tupla3)

    tupla1 = tupla1 + tupla2
    print(tupla1)

def intupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(3 in tupla1)
    print(11 in tupla1)

def iteracaotupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for num in tupla1:
        print(num)

def counttupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2)
    print(tupla1.count(1))
    print(tupla1.count(3))

def stringtuple():
    tupla1 = tuple("Olá mundo!")
    print(tupla1)

def slicetupla():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2)
    print(tupla1[1:3])


"""
It's good to utilize tuples when you don't have to modify the data inside

The access it's similar to lists

We can iterate with the while loop

The worst problem of lists (shallow copy) does not exist
"""
