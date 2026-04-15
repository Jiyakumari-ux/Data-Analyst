marks = {
    "Harry" : 100,
    "Subham" : 56,
    "Rohan" : 78,
     0: "larry"
    }

print(marks.items)
print(marks.keys())
print(marks.values())
print(marks.update({"Harry" : 99, "Renuka" : 88}))
print(marks.get("Harry"))
print(marks.pop("Subham"))
print(marks.popitem())
print(marks.clear())
# The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
# The keys() method returns a view object that displays a list of all the keys in the
# dictionary.
# The values() method returns a view object that displays a list of all the values in the  
#the update() method updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs. It adds the key-value pairs to the dictionary, and if a key already exists, it updates its value.
# The get() method returns the value for the specified key if the key is in the dictionary, otherwise it returns None (or a default value if provided).
# The pop() method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
# The popitem() method removes and returns an arbitrary key-value pair from the dictionary. It raises a KeyError if the dictionary is empty.
# The clear() method removes all items from the dictionary, leaving it empty.