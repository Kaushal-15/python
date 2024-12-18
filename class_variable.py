#class-variable
class phone:
    chargetype="USB-C"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("CHARGER TYPE:",self.chargetype)
#we can modify by using below command:
#phone.chargetype="USB_B"
m1=phone("samsung","20000")
m1.display()
