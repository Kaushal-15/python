#static method
class laptop:
    chargetype="USB-C"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def printPrice(self):
        print(self.price)
    @staticmethod #use decorators to avoid the error for both class and static methods
    def info():
        print("This is the laptop info")

hp=laptop()
hp.setPrice(20000)
hp.printPrice()
hp.info()
