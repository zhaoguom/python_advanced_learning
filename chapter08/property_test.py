from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return self.get_age()

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == "__main__":
    user = User("zhaoguom", date(year=1985, month=12, day=10))
    print(user.get_age())
    print(user.age)
    user.age = 100
    print(user._age)
