# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book():
    def __init__(self, bid = 0, bname = "NA", bprice = 0, bauthor = "NA"):
        self.id = bid
        self.name = bname
        self.price = bprice
        self.author = bauthor
        print("Constructor is called.")

    def showbook(self):
        print("Book id:",self.id)
        print("Book Name:",self.name)
        print("Book price:",self.price)
        print("Book Author:",self.author)

    def __del__(self):
        print("Destructor is called.")

obj1 = Book(1, "Good vibes Good life", 250, "vex king")
obj1.showbook()

obj2 = Book()
obj2.showbook()