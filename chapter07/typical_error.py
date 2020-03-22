class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)
    
    def remove(self, staff_name):
        self.staffs.remove(staff_name)

company1 = Company("company1", ["zhaoguom1", "zhaoguom2"])
company1.add("zhaoguom3")
company1.remove("zhaoguom1")
print(company1.staffs)

company2 = Company("company2")
company2.add("zhaoguom4")

company3 = Company("company3")
company3.add("zhaoguom5")

print(company2.staffs)
print(company3.staffs)
print(company2.staffs is company3.staffs)
print(Company.__init__.__defaults__)