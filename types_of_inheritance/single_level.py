class Phone:
    def __init__(self, brand, model, price):
        self.__price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning the phone")


class Smartphone(Phone):
    pass


phone = Smartphone("Apple", "iPhone 13", 999).buy()
