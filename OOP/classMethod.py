class Employee:
    company = "Apple"

    def show(self):
        print(f"the employee name is a {self.name} and work with {self.company} company")

    @classmethod
    def ChangeCompany(cls,Newcompany):
        cls.company = Newcompany


e1 = Employee()
e1.name = "Ayan"
e1.ChangeCompany("Tesla")
e1.show()