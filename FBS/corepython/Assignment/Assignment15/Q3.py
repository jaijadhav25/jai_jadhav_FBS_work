# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. Showshirt

class Shirt():
    def __init__(self, sid = 0, sname = "NA", stype = "NA", sprice = 0, ssize = "NA"):
        self.id = sid
        self.name = sname
        self.type= stype
        self.price = sprice
        self.size = ssize
        print("Constructor is called.")

    def show_shirt(self):
        print("Shirt id:",self.id)
        print("Shrit name:",self.name)
        print("Shirt type:",self.type)
        print("Shirt price:",self.price)
        print("Shirt size:",self.size)

    def __del__(self):
        print("Destructor is called.")

obj1 = Shirt(101, "Red Tape", "Formal", 2000, "M" )
obj1.show_shirt()

obj2 = Shirt()
obj2.show_shirt()