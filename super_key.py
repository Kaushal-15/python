class a():
    def  __init__(self):
        print("A")
    def dispay(self):
        print("you are in class A")

class b(a):
    def  __init__(self):
        super().__init__()
        print("B") #if this __init__ function is removed then the constructor of A is called .this single inheritance and super keyword
    def dispay(self):
        print("you are in class B")

ob1=b()
