# 迭代器是用来访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器不能返回
# __iter__

from collections.abc import Iterator, Iterable


class Company(Iterable):
    def __init__(self, employee_list):
        self.employee_list = employee_list
    
    def __iter__(self):
        return CompanyIterator(self.employee_list)
    
    def __str__(self):
        return self.employee_list
    

class CompanyIterator(Iterator):
    def __init__(self, employee_list):
        self.employee_list = employee_list
        self.index = 0

    def __next__(self):
        try:
            result = self.employee_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


if __name__ == "__main__":
    company = Company(["zhaoguom1", "zhaoguom2", "zhaoguom3"])
    for com in company:
        print(com)