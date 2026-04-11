a = 31
t = type(a) #class<int>
print(t) #Output: <class 'int'>
b = 3.14
t = type(b) #class<float>
print(t) #Output: <class 'float'>
c = "Hello, World!"
t = type(c) #class<str>
print(t) #Output: <class 'str'>
d = True
t = type(d) #class<bool>
print(t) #Output: <class 'bool'>

e ="31.2"
f = float(e)  # f = e but the type should be float
print(type(e))
print(type(f))