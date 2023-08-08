from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size: yield p


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        print(other)
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    berry = Product('Berry', Color.RED, Size.SMALL)
    plant = Product('Plant', Color.GREEN, Size.MEDIUM)
    car = Product('Car', Color.BLUE, Size.LARGE)

    products = [berry, plant, car]

    pf = ProductFilter()
    print('Filter green products: ')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'{p.name} - {p.color}')

    bf = BetterFilter()
    print('Filter green products better: ')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'{p.name} - {p.color}')

    medium = SizeSpecification(Size.MEDIUM)
    green_medium = AndSpecification(medium, green)
    # OR
    green_medium = green & medium
    for p in bf.filter(products, green_medium):
        print(f'{p.name} - {p.color}')
