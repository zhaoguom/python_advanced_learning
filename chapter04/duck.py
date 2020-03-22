class Cat:
    def say(self):
        print("i'm a cat")


class Dog:
    def say(self):
        print("i'm a dog")


class Duck:
    def say(self):
        print("i'm a duck")

class Company:
    def __init__(self, employee):
        self.employee = employee
    
    def __getitem__(self, item):
        return self.employee[item]
    
    def __len__(self):
        return len(self.employee)

company = Company(["zhaoguom1", "zhaoguom2"])

animal_list = [Cat, Dog, Duck]

for animal in animal_list:
    animal().say()

a = ["bobby1", "bobby2"]
named_tuple = ("bobby3", "bobby4")
s = set()
s.add("bobby5")
s.add("bobby6")
print(a)
a.extend(named_tuple)
print(a)
a.extend(s)
print(a)
a.extend(company)
print(a)