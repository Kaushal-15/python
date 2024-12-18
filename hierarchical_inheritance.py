#hierarchical inheritance
class mom:
    def money(self):
        print("Mother's Money")

class son1(mom):
    pass
class son2(mom):
    pass
class son3(mom):
    pass

s2=son1()
s2.money()
