'''
鸭子类型和抽象基类是整个python语言的基础，python不是通过继承某个类或者接口来实现某些功能，
而是通过实现不同的魔法函数，这样就成为某种类型的对象
抽象基类不能用来实例化对象，它定义了一些函数，继承类必须实现它
'''

class Company:
    def __init__(self, employee):
        self.employee = employee
    
    def __getitem__(self, item):
        return self.employee[item]
    
    def __len__(self):
        return len(self.employee)


from collections.abc import Sized
com = Company(["zhaoguom", "zhaoguom2"])

### 检查某个类是否有某种方法
# option #1
print(hasattr(com, "__len__"))

# option #2
if isinstance(com, Sized):
    print(True)


### 实现一个web框架，集成cache(redis,cache,memorycache)
#需要设计一个抽象基类，指定子类必须实现某个方法
import abc

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()

# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError

# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass

# redis_cache = RedisCache()
# redis_cache.set("key", "value")
