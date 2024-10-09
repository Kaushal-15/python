#list is a python collection data type
#list allows all datatype and also duplicate values
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
a.append(11) #append allows us to add the element in the last of the list
a.append("kaushal")
a.append(11)
a.append(True)
print(a)
a.insert(2,"kaushal")#as we can see that the element is added in the 2nd position by using insert method it will not replace the element
print(a)
a[0]="kaushal"#as we can see that the element is replaced by using square brkets that 1 is replaced by kaushal
print(a)
print(a[4])#we can use square brkets to access the specific element in the list
a.pop(12)#pop removes the element in the list by using index and square brackets
#if we use only a.pop then it will remove the last element in the list
print(a)
b=[11,22,33,44,55]
a.extend(b)#extend method is used to add the list in the list i.e merging two list
print(a)#we can see the output that a and b are merged
print(b)#here we can see that the list b is not changed becausse we have extended a to b so only a has changed
