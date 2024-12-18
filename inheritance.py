class ethernet():
    def internet(self):
        print("Internet is 2.4gb per second")

class phone():
    def Mobile():
        print("Mobile is available")

class laptop(phone):
    def hp(self):
        print("Laptop is available")

ram = laptop()
ram.hp()
ram.Mobile()  #here it is single level inheritance where class laptop can only access the phone class


