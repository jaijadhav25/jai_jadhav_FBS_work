# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product():
    def __init__(self, pid = 0, pname = "NA", pprice = 0, pquantity = 0):
        self.id = pid
        self.name = pname
        self.price = pprice
        self.quantity = pquantity
        print("Constructor is called.")

    def show_product(self):
        print("Product id:",self.id)
        print("Product Name:",self.name)
        print("Product Price:",self.price)
        print("Product Quantity:",self.quantity)

    def __del__(self):
        print("Destructor is called.")

obj1 = Product(102, "Ghar soap", 500, 3)
obj1.show_product()

obj2 = Product()
obj2.show_product()

