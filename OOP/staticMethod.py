

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b


print(Calculator.add(5,6))

#2) Multiple static method 

class Math:

    @staticmethod
    def square(n):
        return n*n

    @staticmethod
    def cube(n):
        return n*n*n

print(Math.square(5))
print(Math.cube(3))