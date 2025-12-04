# Create class Person (name, age); compare 2 Persons by age.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __lt__(self, other):
        return self.__age < other.__age


p1 = Person("Tejas", 22)
p2 = Person("Alex", 25)

if p1 < p2:
    print("p1 is younger.")
else:
    print("p2 is younger or equal.")
