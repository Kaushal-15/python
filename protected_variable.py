#protected variable means that the varibale is hidden and it can be called by child class also (derived class)
class company():
    def __init__(self):
        self._company="Google"
  
class b(company):
    pass

#from the parent class 
c1=company()
print(c1._company)
#printed form the derived class
c2=b()
print(c2._company)
