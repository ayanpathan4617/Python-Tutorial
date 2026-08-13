
# File open for read 

# f = open('myfile.txt','r')
# text = f.read()
# print(text)
# f.close


# File write

# f = open('myfile.txt','w')
# f.write('Hello, world')
# f.close()


# For Read Only One Line

# file = open("myfile.txt",'r')
# print(file.readline())
# file.close()

# For Read Multiple Lines

# file = open("myfile.txt",'r')
# print(file.readlines())
# file.close()

# Writelines

ayan = open("myfile.txt","w")
lines = ["line1 \n","line2 \n","line3 \n","line4 \n"]
ayan.writelines(lines)
ayan.close()