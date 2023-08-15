class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
            return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading')


if __name__ == '__main__':
    db_1 = Database()
    db_2 = Database()
    print(db_1 == db_2)
