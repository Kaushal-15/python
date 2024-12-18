#class-object eg (calculator)

class calculator:
    def __init__(self,A,B):
        self.a=A
        self.b=B
    def add(self):
        print("ADD:",self.a + self.b)
    def sub(self):
        print("SUB:",self.a - self.b)
    def mul(self):
        print("PRODUCT:",self.a * self.b)
    def div(self):
        print("DIVIDE:",self.a / self.b)
    
t1=calculator(2,3)
t1.add()
t1.sub()
t1.mul()
t1.div()
