class Father:
    def show(self):
        print("Father: Progrmming")


class Mother:
    def show(self):
        print("Mother: cooking")

class Child(Father,Mother):
    pass


c = Child()
c.show()      ## First Show Father because father is first argument in chaild class
