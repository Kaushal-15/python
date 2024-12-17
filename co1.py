#class-objects ex
class laptop:
    price=0
    Processor=""
    RAM=""

hp=laptop()
dell=laptop()

hp.price=75000
hp.Processor="i-9"
hp.RAM="16GB"

dell.price=98000
dell.Processor="i-9"
dell.RAM="32GB"

print(f"The price of the hp laptop is {hp.price}")
print(f"The price of the dell laptop is {dell.price}")
print(f"The RAM of the hp laptop is {hp.RAM}")
