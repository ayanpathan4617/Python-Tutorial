
class Student:
    def __init__(self,marks):
        self.marks = marks


    def __add__(self,other):
       return self.marks + other.marks

M = Student(80)
M1 = Student(70)

print(M + M1)




####Common magic methods include:

# __add__(self, other): for the + operator. 
# __sub__(self, other): for the - operator. 
# __mul__(self, other): for the * operator. 
# __eq__(self, other): for the == operator. 
# __str__(self): for string representation (used by print()). 
# __lt__(self, other): for the < comparison operator.