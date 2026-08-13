# Global Varriable
# Access Anywhere

x = 10       # Global Varriable

def my_function():
    print("Hello")
    print(x)

my_function()


# Local Varriable

Y = 55

def ayan():
    print("hii")
    M =  44      # Local Varriable
    print(M)

ayan()
print(Y)

# To change Global varriable

P = 80

def change():
    global P
    P = 50

change()
print(P)