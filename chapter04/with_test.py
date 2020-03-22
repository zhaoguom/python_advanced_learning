# try:
#     f_read = open("hello.txt")
#     print("code started...")
#     # raise KeyError
# except IndexError as e:
#     print("key error")
# else:
#     print("other error")
# finally:
#     print("code ended...")
#     f_read.close()

class Sample:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def do_something(self):
        print("do something")

if __name__ == "__main__":
    with Sample() as sample:
        sample.do_something()