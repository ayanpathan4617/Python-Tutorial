## Single inheritance

class Animal:
    def __init__(self):
        print("Animal is eating ")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat is bark")

C = Cat()

