from datetime import date, datetime
from numbers import Integral

#数据描述符
class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, __):
            raise ValueError("should be integer")
        self.value = value

    def __delete__(self, instance):
        pass

#非数据描述符
class NonDataIntField:
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


if __name__ == "__main__":
    user = User()
    user.age = 30
    print(user.age)
    user.age = "abc"
