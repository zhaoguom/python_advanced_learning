from class_method import Date


class Person:
    '''
    hahaha this is test
    '''
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("imooc")
    print(user.__dict__)
    user.__dict__["school_addr"]="beijing"
    print(user.school_addr)
    print(user.name)
    print(Person.__doc__)
    print(dir(user))
