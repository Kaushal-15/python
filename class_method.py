#class method
class laptop:
    chargetype="USB-C"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def printPrice(self):
        print(self.price)
        
    @classmethod
    def RAM(cls):
        cls.Ram="16Gb"
        print("RAM IS:",cls.Ram)

hp=laptop()
hp.setPrice(20000)
hp.printPrice()
hp.RAM()
