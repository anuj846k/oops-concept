# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print("Now inside a constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buy an phone")


class Smartphone(Phone):
    def buy(self):
        print("Buying an smartphone")


s = Smartphone(20000, "Apple", 13)
s.buy()
