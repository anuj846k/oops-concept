# Pass by reference


# def change(l):
#     print(id(l))
#     l.append(5)
#     print(id(l))


# l = [1, 2, 3, 4]
# print(id(l))
# print(l)


# change(l[:])  # clonning of the list dont send the original list
# print(l)


# Collection of objects


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age


c1 = Customer("anuj", 21)
c2 = Customer("rohan", 22)
c3 = Customer("punit", 21)


l = [c1, c2, c3]

for customer in l:
    print(customer.age, customer.name)
