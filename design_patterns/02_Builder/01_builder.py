class Person:
    def __init__(self):
        self.street_address = None
        self.postcode = None
        self.city = None

        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'{self.street_address}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self):
        super().__init__()

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def money(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb \
        .lives \
        .at('123 London Road') \
        .in_city('London') \
        .with_postcode('SW12BC') \
        .works \
        .at('Fabrikam') \
        .as_a('Engineer') \
        .earning(123000) \
        .build()
    print(p)
    person2 = PersonBuilder().build()
    print(person2)
