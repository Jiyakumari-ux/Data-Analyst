#can you change the value inside a lsit which is contained in set S?
s = {8, 7, 12, "Harry", (1,2)}
# ❌ No, you cannot change the value inside that list — because this set itself is invalid.

# Reason:
# In Python, set elements must be immutable (hashable).
# A list is mutable, so it cannot be stored inside a set.
# This code will give an error:
# TypeError: unhashable type: 'list'
# ✔️ Conclusion:
# The set s = {8, 7, 12, "Harry", [1,2]} is not allowed.
# So modifying the list inside it doesn’t even arise.