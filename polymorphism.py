class animal():
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Birds sings")

d1=dog()
d1.sound()
