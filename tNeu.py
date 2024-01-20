import random

from modules.Person import Person
from modules.Kind import Kind
from modules.EnkelKind import EnkelKind


person1 = Person()
print(person1.crand())

print()

person2 = Kind()
print(person2.crand())

print()

person3 = EnkelKind()
person3.Name = "Sobhan"
person3.FamilienName = "Hassanzadeh"
print(person3.information())

print()

list1 = []
list2 = []

for i in range(1, 11):
    s2 = "person"+str(i)
    s2 = Person()
    list1.append(s2)
print(list1)

for i in list1:
    x = i.crand()
    if x[0] % 2 == 0:
        list1.remove(i)
    else:
        list2.append(x[0])

print(list2)


k = list(person3.information())
k.reverse()
info = k


file = open("C:\\Users\\sobha\\Desktop\\sNeu.txt", 'w')
file.writelines(info)
file.close()
