
## dir() Method   ###see the attributes and methods available for an object, class, or module.
# x = [1,2,3,4]
# print(dir(x))
# print(x.__add__)



## Dict() Method      ##Display all the data in the the form of Dictionary
class Status:
    def __init__(self,name ,age ,color):
        self.name=name
        self.age=age  
        self.color = color

p = Status("Ayan",21,"pink")
print(p.__dict__)


## Help()           ## give description about class , method ,any attributes
print(help(Status))