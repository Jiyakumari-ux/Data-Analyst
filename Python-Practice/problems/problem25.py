#create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. assume that the names are unique.
d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})
print(d)
#if the name of two friends are same , what will happen to the program in problem?
#"last updated value will be shown"
#if the language of two friends are same , whhta will happen to the program?
#"last updated value will be shown but it will contain a problem"