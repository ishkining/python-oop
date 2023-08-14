import copy


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.country}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('test', 0, 'Paris'))
    aux_office_employee = Employee('', Address('aux', 0, 'Paris'))

    @staticmethod
    def __new_employee(proto, name, country):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.country = country
        return result

    @staticmethod
    def new_main_office_employee(name, country):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, country
        )

    @staticmethod
    def new_aux_office_employee(name, country):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, country
        )
