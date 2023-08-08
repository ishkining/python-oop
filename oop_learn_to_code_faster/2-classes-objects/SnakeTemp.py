class Snake:
    """Snake main blueprint"""
    name = 'Anaconda'

    # Method to change name
    def modifyName(self, new_name):
        self.name = new_name


# Objects based on Snake
snake01 = Snake()

# printing on screen
print(snake01.name)

# Modify the name using modifyName
snake01.modifyName('Python')
print(snake01.name)


class Snake:
    """Snake main blueprint"""

    def __init__(self, name):
        self.name = name

    def modifyName(self, new_name):
        self.name = new_name


# Objects
anaconda_roman = Snake('Roman')
anaconda_renat = Snake('Renat')

# printing the value names of instances
print(anaconda_roman.name)
print(anaconda_renat.name)


