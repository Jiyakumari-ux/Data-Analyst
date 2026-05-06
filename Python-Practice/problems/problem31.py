# wap to find the greatest of 4 no. enterd by the user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if(a>=b and a >=c and a>=d):
    print("Greatest number is ",a)
elif(b>=c and b>=d):
    print("Greatest number is ",b)
elif(c>=d):
    print("Greatest number is ",c)
else:
    print("Greatest number is ",d)