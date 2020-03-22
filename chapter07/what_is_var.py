a = 1
a = "abc"
# 先生成对象，然后把a贴上去

a = [1,2,3]
b = a

b.append(4)
print(b)
print(a)
print(a is b)