# __getattr__, 在查找不到属性的时候调用
# __getattribute__, 在查找任何属性的时候无条件进入

from datetime import date

class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info=info

    def __getattr__(self, item):
        return "not find attr"

    def __getattribute__(self, item):
        return "zhaoguom"
    
if __name__ == "__main__":
    user = User("zhaoguom", date(year=1983, month=12, day=12), info={"company":"imooc"})
    print(user.age)
    print(user.birthday)
    