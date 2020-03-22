aList = [3,4,5,6,7,9,11,13,15,17]

print(aList[::])
print(aList[::-1])
print(aList[::2])
print(aList[1::2])
print(aList[3:6])
print(aList[0:100])
print(aList[100:])

aList[len(aList):]=[9]
print(aList)
aList[:0] = [1,2]
print(aList)
aList[3:] = [4,5,6]
print(aList)
aList[::2]=[0]*3
print(aList)
aList[:3]=[]
print(aList)
del aList[::2]
print(aList)
