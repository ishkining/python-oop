class Database:
    _instance = None

    def __init__(self):
        print('Loading data form db')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)
            return cls._instance


if __name__ == '__main__':
    db_1 = Database()
    db_2 = Database()
    print(db_1 == db_2)
