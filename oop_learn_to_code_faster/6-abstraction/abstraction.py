from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print(f'inserted value {x}')

    @abstractmethod
    def task(self):
        print('Hi we are inside Absclass task')


# test child class
class test_class(Absclass):
    def task(self):
        print('Hi we are in test class')


class example_class(Absclass):
    def task(self):
        print('Hi we are in example class')


test_dinaris = test_class()
test_dinaris.task()
test_dinaris.print(50)
