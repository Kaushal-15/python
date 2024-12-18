class a():
    def __init__(self):
        print("A")

    def dispay(self):
        print("you are in class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")  # if this __init__ function is removed, then the constructor of A is called
    def dispay(self):
        print("you are in class B")

class c(b,a):  
    def __init__(self):
        super().__init__()
        print("C")
    def dispay(self):
        print("you are in class C")

ob1 = c()
