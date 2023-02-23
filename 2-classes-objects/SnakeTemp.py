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
