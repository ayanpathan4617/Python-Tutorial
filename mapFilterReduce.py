
# Map function
def square(x):
    return x * x

numbers = [1,2,3,4,5,6,7,8]
result = map(square,numbers)
print(list(result))

# Convert string tto integer

name = ["10","20","30","40"]
result = map(int,name)
print(list(result))  

# find length of each length

string = ["Ayan", "Pathan", "Data"]
result = map(len,string)
print(list(result))


##/////////// FILTER Function  /////////////##

def even(num):
    return num%2 ==0

number = [1,2,3,4,5,6,7,8,9]
result = filter(even,number)
print(list(result))


##//////////  Reduce Function  ////////////##

from functools import reduce
def sum(a,b):
    return a+b

list = [1,2,3,4,5] 
result = reduce(sum,list)
print(result) 


