#dicyionary are key value-pairs
a={
    "name":"john",
    "age":1,
    "location":["erode","chennai","cbe","salem"]
}
print(a)
a["age"]=2
print(a)
a["mark"]=98
print(a)
a.update({"age":4})
print(a)
a.pop("mark")
print(a)
del a["age"]
print(a)
a.clear()
print(a)
