'''
#### 问题
- 回调模式编码复杂度高
- 同步编程的并发性不高
- 多线程编程需要线程间同步 lock ，导致降低性能

#### 方案
- 采用同步的方式去编写异步的代码
- 使用单线程去切换任务
    - 线程是由操作系统切换的，单线程切换意味着需要程序员自己去调度任务
    - 不再需要锁，并发性高，单线程内的函数切换性能远高于线程切换，并发性更高
- 协程：可以暂停的函数，并且可以从暂停的地方传入值
'''

def gen_func():
    #1. 可以产出值 2. 可以接收值
    html = yield "http://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "zhaoguom"

if __name__ == "__main__":
    gen = gen_func()
    url = next(gen)
    html = "zhaoguom"
    # 启动生成器的方式有2中，next(), send()
    # send()方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield
    print(gen.send(html))
