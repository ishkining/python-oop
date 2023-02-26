class Person:
    """ Person main blueprint """

    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print(f'Hi, my name is {self.name}'
              f', and my age is {self.age}'
              f', and my personID is {self.personID}')


person_olina = Person('Olina', 22, 150)
person_alina = Person('Alina', 23, 190)
person_diana = Person('Diana', 37, 180)

person_alina.display_data()
person_olina.display_data()
person_diana.display_data()
