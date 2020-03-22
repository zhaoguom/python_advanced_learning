a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a is b)
print(a == b)

a = 1
b = 1
print(a is b)
print(a == b)

a = 'abc'
b = 'abc'
print(a is b)
print(a == b)


class People:
    pass


person = People()

print(type(person) is People)
print(isinstance(person, People))
