from itertools import chain

my_list = [1,2,3]
my_dict = {"zhaoguom1":"http://www.baidu.com", 
"zhaoguom2":"http://www.imooc.com"}

def my_chain(*args, **kwargs):
    for my_interable in args:
        yield from my_interable
        # for value in my_interable:
        #     yield value

for i in my_chain(my_list, my_dict, range(6,10)):
    print(i)

def g1(iterable):
    yield iterable

def g2(iterable):
    yield from iterable

for i in g1(range(10)):
    print(i)

for i in g2(range(10)):
    print(i)


