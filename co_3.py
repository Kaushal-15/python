#class-objects eg
class student:
    def __init__(self):
        self.name=""
        self.register=""
    def display(self):
        print("Name:",self.name)
        print("RegNO:",self.register)

s1=student()
s2=student()

s1.name="kaushal"
s1.register="15"

s2.name="MANOJ"
s2.register="9"

s1.display()
print("************************")
s2.display()
