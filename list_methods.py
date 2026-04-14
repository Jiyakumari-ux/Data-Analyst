friends = ['Apple', "Cherry", 5, 234.67, False, "Aakash", "Rohan"]
print(friends)

friends.append("Harry") #append is used to add a new element at the end of the list)
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
l1.sort() #sort is used to sort the list in ascending order
print(l1)
l1.reverse() #reverse is used to reverse the order of the list
print(l1)
friends.insert(3, 33333) #insert is used to add a new element at the specified index
print(friends)
friends.remove(33333) #remove is used to remove the first occurrence of the specified element from the list
print(friends)
l1.pop(3) #pop is used to remove the element at the specified index and return it. If no index is specified, it removes and returns the last element of the list.
print(l1)
print(l1.pop(3)) #pop is used to remove the element at the specified index and return it. If no index is specified, it removes and returns the last element of the list.
l2 = [1, 34, 62, 2, 6, 11, 6, 6]
print(l2.count(6)) #count is used to count the number of occurrences of the specified element in the list
print(l2.index(62)) #index is used to find the index of the first occurrence of the specified element in the list. If the element is not found, it raises a ValueError.
print(l2.extend([100, 200, 300])) #extend is used to add all the elements of the specified iterable (e.g., list, tuple, set) to the end of the list
l3 = [10, 0, 560, 5]
new_list = l3.copy() #new_list is used to create a new list from the specified iterable (e.g., list, tuple, set)
print(new_list)#copy is used to create a shallow copy of the list. It returns a new list that contains the same elements as the original list, but it is a separate object in memory. Changes made to the copied list will not affect the original list, and vice versa.
print(l2.clear()) #clear is used to remove all the elements from the list, resulting in an empty list.