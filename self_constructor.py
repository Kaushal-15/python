#self constructor
class laptop:
    price=0
    RAM=""
    def __init__(self):
        self.RAM=""
        self.Proc=""
    def display(self):
        print("RAM:",self.RAM)
        print("PROCESSOR:",self.Proc)

hp=laptop()
hp.RAM="16Gb"
hp.Proc="I-9"

hp.display()
