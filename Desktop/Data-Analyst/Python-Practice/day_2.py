num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)   

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest:", max(a, b, c))

text = input("Enter a string: ")
vowels = "aeiou"

count = 0
for char in text.lower():
    if char in vowels:
        count += 1

print("Vowel count:", count)