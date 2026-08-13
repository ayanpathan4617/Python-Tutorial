

#Print number from 1 to 10;
for i in range(1,11):
    if(i==6):
        break
    print(i)


#Print number from 5 to 1;

for roll in range(1,11):
    if(roll == 6):
        print("Student is found")
        break
    print("Checking roll no", roll)



##Continued Statement

for i in range(1,11):
    if(i==5):
        continue
    print(i)



for roll in range(1,21):
    if(roll == 10):
        continue
    print("checking roll no", roll)




# Function 
# User-defined func

def greet():
    print("My name is ayan pathan")
greet    