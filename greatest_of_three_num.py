a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>=b and a>=c:
    greatest=a
elif b>=a and b>=c:
    greatest=b
else:
    greatest=c
    print(f"The greatest numeber is {greatest}")
