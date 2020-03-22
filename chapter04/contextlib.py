import contextlib

@contextlib.contextmanager
def file_open(filename):
    print("file open")
    yield {}
    print("file end")

with file_open("duck.py") as f:
    print("hello")