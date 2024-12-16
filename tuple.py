#tuple doesnt allow us to add or remove the elements 
a=(1,2,34,5,5)
b=list(a)#so we can do casting to change it as a list
b.pop()
b.insert(0,11)
b.append(11)
b.append(3)
b[3]=4
print(b)
