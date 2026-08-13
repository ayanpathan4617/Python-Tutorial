

class Person:
    name = "Ayan"
    occupation = "Python Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
 
a = Person()


a.name = "Pathan"              #For change name and occupation in class
a.occupation = "Data Analyst"
a.info()



