# Parent class
class Person:
    def person_data(self, name, age):
        print('hello from the Person class')
        print(f'Name: {name} and Age: {age}')


# Company class
class Company:
    def company_data(self, comp_name, location):
        print('hello from the Company class')
        print(f'Company name is {comp_name} and location is {location}')


# Child class
class Employee(Person, Company):
    def employee_data(self, salary, skill):
        print('hello from the Company class')
        print(f'Salary is {salary} and skill is {skill}')


# Object employee
employer_ramil = Employee()
employer_ramil.person_data('Ramil', '22')
employer_ramil.company_data('MTS', '30K')
