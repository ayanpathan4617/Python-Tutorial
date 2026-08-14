
class Employee:
    company = "Apple"             ## Class Varriable
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        print(f"the name of employee is {self.name} and rise amount is {self.raise_amount} and company name is {self.company} ")


s1 = Employee("Ayan")
s1.name = "rahul"
s1.showDetails()   #in these case not company are call so by default directly class varriable are call


s2 = Employee("pathan")
s2.company = "Goggle"   #in these case we are call the instance varriable
s2.showDetails()