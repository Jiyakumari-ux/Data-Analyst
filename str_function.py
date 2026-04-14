name = "harry potter" 
print(len(name))
print(name.endswith("rry"))
print(name.startswith("Ha"))
print(name.capitalize())
print(name.count)
print(name.find("r"))
print(name.replace("r","p"))
print(name.upper())
print(name.strip()) #remove space from both sides of the string
print(name.lower())
print(name.split(",")) #split the string into a list of substrings based on the specified separator, in this case, a comma. If the separator is not found in the string, it will return a list containing the original string as its only element.
print(name.isdigit()) #returns True if all characters in the string are digits, and False otherwise.
print(name.isalpha()) #returns True if all characters in the string are alphabetic, and
print("-".join(name)) #returns a string that is the concatenation of the strings in the iterable, separated by the string on which it is called. In this case, it will concatenate the characters of the string "harry" with itself, resulting in "hhaarrvvy".