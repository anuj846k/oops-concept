class Phone:
    def __init__(self, brand, model, price):
        print("Inside a phone constructor")
        self.__price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a phone")


class Product:
    def review(self):
        print("This is a product review")


class Smartphone(Phone, Product):
    pass


s = Smartphone("Apple", "iPhone 13", 999)
s.buy()
s.review()



# MRO Method Resolution Order is the order in which you pass classes in the class definition. In the above example, we have passed Phone first and then Product. So, when we call the buy method, it will look for the buy method in the Phone class first and then in the Product class. If we had passed Product first and then Phone, it would have looked for the buy method in the Product class first and then in the Phone class.

