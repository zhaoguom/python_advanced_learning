import numbers

class Group:
    #支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)
    
    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __str__(self):
        return ','.join(self.staffs)
            

staffs = ["zhaoguom1", "zhaoguom2", "zhaoguom3", "zhaoguom4"]
group = Group(group_name="user", company_name="imooc", staffs=staffs)
print(group)
sub_group = group[:2]
print(sub_group)
print(group[0])
print(len(staffs))
result = True if "zhaoguom" in group else False
print(result)

for g in group:
    print(g)
