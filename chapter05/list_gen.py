data = [x for x in range(20) if x%2==1]
print(data)

data = (x*x for x in range(20) if x%2==1)
print(data)
for x in data:
    print (x, end=' ')

print()
my_dict = {"zhaoguom":3, "fannie":1, "iris":1}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)