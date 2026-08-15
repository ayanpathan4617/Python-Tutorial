
###Super() with constructor
class Employee:
    def __init__(self,name ,id):
        self.name = name
        self.id = id
       

class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name = name
        # self.id = id
        super().__init__(name,id)
        self.lang = lang


e1  = Employee("ayan",200)
e2 = Programmer("rohan",300,"Python")

print(e1.name,e1.id)
print(e2.name,e2.id,e2.lang)






## Super with Method

class Animal:
    def show(self):
        print("Animal is eating ")

class Dog(Animal):
    def show(self):
        super().show()    ## First call animal Class
        print("Dog is barking")

d = Dog()
# print(d.show())
d.show()




