class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


if __name__ == "__main__":
    s1 = Singleton("First Instance")
    print(s1.get_value())

    s2 = Singleton("Second Instance")
    print(s2.get_value())  # Output: First Instance

    print(s1 is s2)  # Output: True