class Test:
    class_var = 10  # Class variable

    def __init__(self, value):
        self.instance_var = value  # Instance variable

obj1 = Test(20)
obj2 = Test(30)

obj1.class_var = 50
print(obj2.class_var)  