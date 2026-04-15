#check that a type cannot be changed in python
a = (34, 234, "Harry")

a [2] = "Larry" # This will give an error because tuples are immutable in Python, meaning their elements cannot be changed after they are created.