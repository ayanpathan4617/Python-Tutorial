class Grandfather:
    def property(self):
        print("Grandfathers property")


class Father(Grandfather):
    def car(self):
        print("father drive car")

class Son(Father):
    def study(self):
        print("Son has Study")

s = Son()
s.property()
s.car()
s.study()


