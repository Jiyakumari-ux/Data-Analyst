marks = {
    "Harry" : 100,
    "Subham" : 56,
    "Rohan" : 78,

}

print(marks, type(marks)) # This will print the dictionary and its type
print(marks["Harry"]) # This will print the value associated with the key "Harry"   
print(marks[0]) # This will give an error because dictionaries are not indexed by position, they are indexed by keys.

# To access the value of a key, we use the key itself, not an index.
#dictionaries are unordered collections of key-value pairs,
#so we cannot access them using an index like we do with lists.
#Instead, we use the keys to access the corresponding values.

#properties of dictionaries:
#1. Dictionaries are mutable, which means we can change their content after they have been created.
#2. Dictionaries are unordered, which means that the items do not have a defined order.
#3. Dictionaries are indexed by keys, which can be of any immutable type (like strings
#   or numbers), and the values can be of any type.
# cannot have duplicate keys in a dictionary, but can have duplicate values.