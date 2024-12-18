class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print(f"The name,salary and age of the Manager is {self.name},{self.salary},{self.dept}")

m1=Manager("john","20000","CSE")
m1.display()
