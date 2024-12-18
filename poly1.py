#polymorphism and inheritance eg
class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self,l,b):
        print("The area of th rectangle is:",l*b)

rect=rectangle()
rect.area(3,4)
