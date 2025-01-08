a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
big = a if(a>b and a>c) else b if(b>c) else c
print(f"The greatest number is {big}")