from itertools import chain

my_list = ["zhaoguom1", "zhaoguom2"]
my_dict = {"zhaoguom3":"https://www.sina.com.cn", "zhaoguom4":"https://www.imooc.com"}

for value in chain(my_list, my_dict, range(5, 10)):
    print(value, end=" ")

def my_chain(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value


def my_chain2(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable

print()

for value in my_chain2(my_list, my_dict, range(5, 10)):
    print(value, end=" ")

print()

def g1(iterable):
    yield iterable

def g2(iterable):
    yield from iterable

for value in g1(range(10)):
    print(value, end=" ")

print()

for value in g2(range(10)):
    print(value, end=" ")

print()
'''
#1. main：调用方；g3：委托生成器；gen：子生成器
#2. yield from会在调用方与子生成器建立一个双向通道，
'''
def gen():
    yield 1
    yield 2

def g3(gen):
    yield from gen

if __name__ == "__main__":
    g = g3(gen())
    print(g.send(None))
    print(g.send(None))
    print(g.send(None))