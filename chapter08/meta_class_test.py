# python中类的实例化过程，会首先寻找metaclass，通过metaclass来创建类(包括基类)
# 如果没有找到，那么就通过type来创建
from collections.abc import *

class MetaClass(type):
    def __new__(cls, *args, **kargs):
        print("in meta class")
        return super().__new__(cls, *args, **kargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


if __name__ == "__main__":
    user = User("zhaoguom")
    print(user)

