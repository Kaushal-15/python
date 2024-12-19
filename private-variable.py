#private variable(encapsulation)-access modifiers
class company():
    def __init__(self):
        self.__company="Google"
    def display(self):
        print(self.__company)
c1=company()
c1.display()

# print(c1.__company)
#if the above statement is executed it will show error because private variable can only accessed inside the class
