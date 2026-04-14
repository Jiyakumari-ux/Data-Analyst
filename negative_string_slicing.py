name = "Harry"

print(name[0:3])

print(name[-4: -1])

print(name[1:4]) # aap neagtive index ko corresponding positive index me convert krlo [-4 : -1] = [1:4] kyuki h ka index 0 hai aur r ka index 3 hai to a ka index 1 hai aur y ka index 4 hai

print(name[ : 3]) #is same as print(name[0:3])

print(name[1: ]) #is same as print(name[1:5]) kyuki name me 5 character hai aur last index 4 hai to 1 se start krke 4 tk print hoga

# slicing with skip value

a ="0123456789"
print("a: ", a[1:7:3]) #14

#kese hota h ye sikho 
b ="abcdefghijklmnopqrstuvwxyz"

print("b: ",b[1:9:4]) #output bf

#kese aaya ye dekhte hai 
b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:9]) #output bcdefghi
#dekho pehla b to aayega hi uske baad last me 4 likha h to 4 steps aage aana h or value likhna h to b ke baad c,d,e,f,g,h,i aayenge to 4 steps aage aane par f aayega to output bf hoga

c ="0123456789"
print("c: ",c[0:8:2])# ouput aayega 012345678
#0 se 2 step aage bdte jana h to aayega 0,2,4,6,8 aayega to output 02468 hoga

word = "amazing"
print(word[1:6:2]) #output mzn