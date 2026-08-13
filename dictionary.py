dic = {
    "name":"ayan", 
    "age": "22",
    "roll no": "27"
    }

print(dic)
print(dic["name"])
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(key)


# Methods

student = {"name":"ayan", "age":20, "course":"ECE"}
print(student)
print(student.keys())
print(student.values())
print(student["name"])

student.pop("course")
print(student)

student.popitem()
print(student)