class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.denom = d

    def __str__(self):
        # This method is here is overloading using magic method. Whenever we try to print the object of the class, it will call the __str__ method and return the string representation of the object.
        return "{}/{}".format(self.num, self.denom)

    def __add__(self, other):
        temp_num = self.num * other.denom + other.num * self.denom
        temp_denom = self.denom * other.denom
        return "{}/{}".format(temp_num, temp_denom)

    def __sub__(self, other):
        temp_num = self.num * other.denom - other.num * self.denom
        temp_denom = self.denom * other.denom
        return "{}/{}".format(temp_num, temp_denom)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_denom = self.denom * other.denom
        return "{}/{}".format(temp_num, temp_denom)


x = Fraction(2, 3)
y = Fraction(4, 5)
print(x + y)
print(x * y)
