name=[1,2,3,"text",True]
name.append(4)
print(name)

print(name.index("text"))

print(name.count("text"))

name.insert(3,4)
print(name)

name.pop()
print(name)

var=[1,8,4,7]
var.sort()
print(var)

var1=["text","helo","hi"]
var1.sort()
print(var1)

var2=[1,4,5]
var3=[5,8,9]
var2.extend(var3)
print(var2)