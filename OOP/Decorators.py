def decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")

    return wrapper

@decorator
def hello():
    print("hello,Ayan")


hello()


## Decorators With Parameters


def decorators(func):
    def wrapper(*args,**kwargs):
        print("function started")
        result = func(*args,**kwargs)
        print("Function finished")

        return result
    return wrapper

@decorators
def add(a,b):
    return a+b

print(add(50,50))