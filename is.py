a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True (values are the same)
print(a is c)  # False (different objects in memory)
print(a is b)  # True (same object in memory)