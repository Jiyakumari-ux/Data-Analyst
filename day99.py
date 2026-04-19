a = (1, 45, 342, 3424, False, "Rohan", "Shivam", 5.67)
print(type(a))

no = a.count(45) #count is used to count the number of occurrences of the specified element in the tuple
print(no)
print(a.index("Rohan")) #index is used to find the index of the first occurrence of the specified element in the tuple. If the element is not found, it raises a ValueError.
print(a[0]) #indexing in tuple
print(a[0:4]) #slicing in tuple
b = (23, 567, "harry")
print(a +b) #concatenation of tuples
print(a*2)