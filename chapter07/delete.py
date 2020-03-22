a = object()
b = a 

del a
print(b)
print(a)

class A:
    def __del__(self):
        pass

