# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


person_flarit = Person('Flarit', 22)

# Getting private age
print(f'Name: {person_flarit.name}, {person_flarit.get_age()}')

# Setting private age
person_flarit.set_age(23)

# Getting private age
print(f'Name: {person_flarit.name}, {person_flarit.get_age()}')
