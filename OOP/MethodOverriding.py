class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius *self.radius
    

d = Shape(3,5)
print(d.area())


C = Circle(5)
print(C.area())



#### with Super class

class Animal:
    def sound(self):
        print("Animal make a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()


