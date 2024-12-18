#Instance variable
class phone:
    def __init__(self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
    def display(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("CHARGER TYPE:",self.chargetype)

m1=phone("samsung","20000","USB-C")
m1.display()
