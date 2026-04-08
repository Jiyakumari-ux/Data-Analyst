# find out and differentiate between even and odd numbers

numbers = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda x: x % 2 == 0, numbers)))  # even numbers
