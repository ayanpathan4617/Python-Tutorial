

# Getter Method
# class Student:
#     def __init__(self,name):
#          self.name = name

#     def get_name(self):
#          return self.name


# s1 = Student("Ayan")
# print(s1.get_name())



## Setter Method
class Student:
    def __init__(self,name):
         self.name = name

    def get_name(self):
         return self.name

    def set_name(self,name):
         self.name = name

s1 = Student("Ayan")
print(s1.get_name())

s1.set_name("rahul")
print(s1.get_name())
