s = set({1,2,3,4,5,6,7,7})
print(type(s))
print(s)

if 3 in s:
    print("Foi")
else:
    print("Ferrou")

a = set({10,10,9,8,7,6,5,4,3,2,1})
print(a)

for b in a:
    print(b)
a.add(11)
print(a)
a.remove(1)
print(a)
a.discard(123)
print(a)

novo = a.copy()
novo2 = a

a.remove(2)

print(novo)
print(novo2)

e_python = {"Fernando", "Julia", "Carol"}
e_java = {"Carol", "Fernanda", "Julia"}

e = e_python.union(e_java)
print(e)