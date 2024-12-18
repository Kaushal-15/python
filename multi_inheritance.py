class ethernet():
    def internet(self):
        print("Internet is 2.4gb per second")

class phone(ethernet):
    def Mobile(self):
        print("Mobile is available")

class laptop(phone):
    def hp(self):
        print("Laptop is available")

ram = laptop()
ram.hp()
ram.Mobile()  #here it is multi level inheritance where class laptop has the phone class access but the phone class has the 
                                        # access to the ethernet so laptop can also access the ethernet class
ram.internet()

