class Phone:
    def __init__(self, brand, model, price):
        print("Inside a phone constructor")
        self.__price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning the phone")


class Smartphone(Phone):
    pass


class Product(Phone):
    pass


s = Smartphone("Apple", "iPhone 13", 999)
p = Product("Apple", "iPhone 13", 999)
s.buy()
p.return_phone()
