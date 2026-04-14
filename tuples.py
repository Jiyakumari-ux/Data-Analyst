#tuple is an immutable data structure in Python that can hold a collection of items.
# It is similar to a list, but unlike lists, tuples cannot be modified after they are created.
# Tuples are defined using parentheses () and can contain elements of different data types.
a =(1, 2, 5, 6, 9)
print(type(a))
b=(1)
print(type(b)) #Output: <class 'int'> because it is not a tuple it is an integer
c=(1,) #to create a tuple with a single element we need to add a comma after the element
print(type(c)) #Output: <class 'tuple'> because it is a tuple with a single element

d = (1, 45, 342, 3424, False, "Rohan", "Shivam", 5.67)
print(type(d))