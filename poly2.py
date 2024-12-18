class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(f"The name and grade is:{self.name},{self.grade}")

s1=student("John","A")
s1.display()
