#class-object-2
class laptop:
    price=0
    RAM=""
    def __init__(self):
        self.price=0
        self.RAM=""
        self.Proc=""
    def display(self):
        print("Display")

hp=laptop()
hp.price=80000
hp.RAM="16Gb"
hp.Proc="I-9"
print(hp.price)
