class Grandfather:
    def property(self):
        print("Grandfathers property")


class Father(Grandfather):
    def car(self):
        print("father drive car")

class Son(Father):
    def study(self):
        print("Son has Study")

class Brother(Son,Father):
    def play(self):
        print("Brother playing cricket")

B = Brother()
B. property()
B.car()
B.study()
B.play()