tuple1=("ram","shyam","mohan")
print("öriginal tuple",tuple1)

list1=list(tuple1)
print("original list",list1)

list1.insert(3,"krishna")
print("changed list",list1)

tuple2=tuple(list1)
print("adding new value",tuple2)