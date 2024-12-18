#class-object eg
class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.regno)

t1=teacher("Manoj","9")
t2=teacher("john","22")

t1.display()
t2.display()
