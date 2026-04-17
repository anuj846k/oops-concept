class Geometry:
    def area(self, a, b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b


obj = Geometry()
print(obj.area(3, 4))


# in python technically
# does not support method overloading. The second definition of the area method will overwrite the first one. So, when we call obj.area(3), it will raise a TypeError because the area method is expecting two arguments (length and breadth) but we are only passing one argument (radius).
# To achieve method overloading in python, we can use default arguments. In the above example, we have defined the area method with two parameters (a and b) and we have assigned a default value of 0 to the second parameter (b). So, when we call obj.area(3), it will use the default value of b which is 0 and it will calculate the area of a circle using the formula 3.14 * a * a. When we call obj.area(3,4), it will calculate the area of a rectangle using the formula a * b.
