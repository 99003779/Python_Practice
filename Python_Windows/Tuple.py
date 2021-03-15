##Tuple are similar to list but are immutable
##A tuple is a read only data structure in which size and value of the items can't be modified
##Tuples are enclosed in paranthesis
tup = ("Hi","python",2)

print(type(tup))
print(tup)
print(tup*3)
print(tup[2])
print(tup[0:1])
print(tup[1:])
print([tup + tup])
tup[1] = "change"
print(tup)