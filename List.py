# lists are  containers to store a set of values of any data type.
# list are mutable
# list are ordered
# list are defined by using square brackets []
# list can contain duplicate values
# list can contain values of different data types
# list can be nested
#list cane be indexes just like a string

friends = ['Apple', "Cherry", 5, 234.67, False, "Aakash", "Rohan"]

print(friends[0])

friends[0] = "Grapes" #unlike string we can change the value of list by using index because list are mutable
print(friends[0])
print(friends[0:4]) #slicing in list
print(friends[-4: ]) #slicing in list with negative index
