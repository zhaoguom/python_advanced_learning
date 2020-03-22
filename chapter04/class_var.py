class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 11
a.aa = 100
print(a.aa, a.x, a.y)
print(A.aa)