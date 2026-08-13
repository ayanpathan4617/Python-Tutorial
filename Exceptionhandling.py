# num  = int(input("Enter the number:"))
# print(f"Multiplication table of {num} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(num)} X {i} = {int(num)*i}")

# except:
#     print("Invalid Input")


# 2) problem

try:
    num = int(input("Enter an integr"))
    a = [6,3,7]
    print(a[num])
except ValueError:
    print("Numbered enter is not an integer.")

except IndexError:
    print("Index Error")