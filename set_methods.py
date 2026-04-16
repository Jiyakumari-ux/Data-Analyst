s ={1, 5, 32, 54, 5, 5,5, "Harry"}
print(s, type(s))

#set methods
#1. add() - This method is used to add an element to the set. If the element already exists, it will not be added again.
#2. remove() - This method is used to remove a specific element from the set. If the element does not exist, it raises a KeyError.
#3. discard() - This method is used to remove a specific element from the set.If the element does not exist, it does nothing (no error is raised).
#4. pop() - This method is used to remove and return an arbitrary element from theset. If the set is empty, it raises a KeyError.
#5. clear() - This method is used to remove all elements from the set, leaving it empty.
#6. union() - returns a new set with all items from both sets.
#7. intersection() - returns a set which contains only item in both sets.
print(len(s))
s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s)) #alt shirt arrow to copy the same line in downward or upward direction
