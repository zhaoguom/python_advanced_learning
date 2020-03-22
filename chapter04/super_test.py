class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

from threading import Thread
class MyThread(Thread):
    def __init__(self, user, name):
        self.user = user
        super().__init__(name=name)


if __name__ == "__main__":
    b = B()
