# 生成器是可以暂停的函数，是有状态的

#协程
def gen_func():
    # 1. 返回值给调用方；2.调用方通过send方式返回值给gen
    _value = yield 1
    return "zhaoguom"
#1. 用同步的方式编写异步的代码，在适当的时候暂停函数或者启动函数

import inspect
if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))