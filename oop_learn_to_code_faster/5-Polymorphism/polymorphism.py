def add(x, y, z=0):
    return x + y + z


print(add(5, 3))
print(add(5, 3, 2))


class Bird:
    def intro(self):
        print('Hi, that is Bird class!')

    def flight(self):
        print('Most of the birds can fly but some cannot')


class Sparrow(Bird):
    def flight(self):
        print('Sparrow can fly!')


class Ostrich(Bird):
    def flight(self):
        print('Ostriches cannot fly!')


bird_roman = Bird()
sparrow_olina = Sparrow()
ostrich_alina = Ostrich()

bird_roman.intro()
bird_roman.flight()

sparrow_olina.intro()
sparrow_olina.flight()

ostrich_alina.intro()
ostrich_alina.flight()
