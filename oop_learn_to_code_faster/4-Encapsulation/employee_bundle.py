class Employee:
    # class constructor
    def __init__(self, name, salary, project):
        self.__name = name
        self._salary = salary
        self.project = project

    def show_details(self):
        print(f'Name is {self.__name}, salary is {self._salary}, project is {self.project}')

    def work(self):
        print(f'{self.__name} is working on {self.project}')


empoyer_almaz = Employee('Almaz', 35000, 'Fixing Computers')
empoyer_almaz.show_details()
empoyer_almaz.work()