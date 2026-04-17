class Product:
    def review(self):
        print("This is a product review")


class Phone(Product):
    def __init__(self, brand, model, price):
        self.__price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):
    pass


s = Smartphone("Apple", "iPhone 13", 999)
p = Smartphone("Apple", "iPhone 13", 999)
s.buy()
s.review()
p.review()
